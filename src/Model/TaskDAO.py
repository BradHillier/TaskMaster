import sqlite3

from User import User
from Task import Task
from TaskList import TaskList

from TaskSerializer import TaskSerializer


class TaskDAO:

    def __init__(self, db: str):
        self.db = db
        self.serializer = TaskSerializer()

    def create(self, task_list, **kwargs):

        # default values
        attrs = {
            'listID': task_list.ID,
            'username': task_list.user.username,
            'taskName': None,    
            'description': None, 
            'dueDate': None,     
            'isCompleted': False, 
            'priority': None
        }
        required = ('taskName', 'dueDate')

        # update the default values with those passed by the caller
        for key in attrs.keys():
            if key in kwargs:
                attrs[key] = kwargs[key]
            elif key in required:
                print(f'Error: missing key, "{key}" is required')

        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Tasks (listID, username, taskName, description, dueDate, isCompleted, priority)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [key for key in attrs.values()])
            conn.commit()

    def getTasks(self, task_list: TaskList):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            res = cur.execute( """
                SELECT *
                FROM Tasks
                WHERE listID = (?)
            """, [task_list.ID])

            for task in res.fetchall():
                task_list.tasks.append(self.serializer.deserialize(task))

    def update(self, task, **kwargs) -> Task:
        pass

    def delete(self, task_list: TaskList, task: Task):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM Tasks
                WHERE taskID = (?)
            """, [task.ID])
            conn.commit()
        task_list.tasks.remove(task)


if __name__ == '__main__':
    myUser = User(username='test_user', email='user@example.com')
    myList = TaskList(ID=1, name='Inbox', user=myUser) 

    myDAO = TaskDAO('../../database.sqlite3')

    # Create a task
    print('checking if a task can be created')
    task_data = {
            'taskName': 'my test task',
            'dueDate': '2023-04-05'
    }
    myDAO.create(myList, **task_data)

    # check if the previously created task is in the task list
    myDAO.getTasks(myList)
    myTask = [task for task in myList.tasks if task.name == 'my test task']
    assert myTask[0].name == 'my test task' 
    assert len(myTask) == 1

    # check if the previously created task was properly deleted
    print('checking if a task can be deleted')
    myDAO.delete(myList, myTask[0])
    matches = [task for task in myList.tasks if task.name == 'my test task']
    assert len(matches) == 0
