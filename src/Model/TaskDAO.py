import sqlite3
from dataclasses import dataclass
from datetime import date
import dateparser


@dataclass
class User:
    username: str
    email: str

@dataclass
class Task:
    ID: int
    listID: int
    user: str # change to User obj
    name: str
    description: str
    dueDate: date
    isCompleted: bool
    priority: str

class TaskList:

    def __init__(self, ID: int, name: str, user: User):
        self.ID = ID
        self.name = name
        self.user = user
        self.tasks = []


def deserialize(task_data: tuple) -> Task:
    return Task(
        ID = task_data[0],
        listID = task_data[1],
        user = task_data[2],
        name = task_data[3],
        description = task_data[4],
        dueDate = dateparser.parse(task_data[5]),
        isCompleted = task_data[6],
        priority = task_data[7])



class TaskDAO:

    def __init__(self, db: str):
        self.db = db

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
                task_list.tasks.append(deserialize(task))

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

    myDAO = TaskDAO('test.db')

    task_data = {
            'taskName': 'my test task',
            'dueDate': '2023-04-05'
    }
    myDAO.create(myList, **task_data)
    myDAO.getTasks(myList)

    # check if the previously created task is in the task list
    print('checking if a task can be created')
    myTask = [task for task in myList.tasks if task.name == 'my test task']
    assert myTask[0].name == 'my test task' 
    assert len(myTask) == 1


    # check if the previously created task was properly deleted
    print('checking if a task can be deleted')
    myDAO.delete(myList, myTask[0])
    matches = [task for task in myList.tasks if task.name == 'my test task']
    assert len(matches) == 0




