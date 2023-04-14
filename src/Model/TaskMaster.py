import copy
from src.Model.TaskDAO import TaskDAO
from src.Model.TaskListDAO import TaskListDAO

from src.Model.User import User
from src.Model.Task import Task
from src.Model.TaskList import TaskList

class TaskMaster:

    def __init__(self):
        self.user = User(username='test_user', email='user@example.com')
        self.database = 'database.sqlite3'

        # data access objects
        self.task_dao = TaskDAO(self.database)
        self.task_list_dao = TaskListDAO(self.database)

        self.all_lists: list[TaskList] = self.task_list_dao.getAll(self.user.username)
        self.current_list: TaskList = self.all_lists[0]

    def getCurrentList():
        copy.deepycopy(self.current_list)

    def changeList(self, task_list: TaskList):
        self.current_list = task_list
        if len(task_list) == 0:
            self.current_list.extend(self.task_dao.getTasks(task_list.ID))

    def createTask(self, **kwargs):
        task_id = self.task_dao.create(**kwargs)
        if task_id != None:
            new_task = self.task_dao.getTask(task_id)
            self.current_list.append(new_task)

    def toggleTaskCompleted(self, task: Task):
        self.task_dao.update(task.ID, isCompleted = not task.isCompleted) 
        task.isCompleted = not task.isCompleted

    def updateTask(self, task: Task, **kwargs):
        self.task_dao.update(task.ID, **kwargs)

    def deleteTask(self, task: Task):
        self.task_dao.delete(task.ID)
        for task_list in self.all_lists:
            if task_list.ID == task.listID:
                task_list.remove(task)

    def createList(self, name: str):
        list_id = self.task_list_dao.create(self.user.username, name)
        if list_id != None:
            new_list = self.task_list_dao.getOne(list_id)
            self.all_lists.append(new_list)

    def renameList(self, task_list: TaskList, name: str):
        self.task_list_dao.rename(task_list.ID, name)
        task_list.name = name

    def deleteList(self, task_list: TaskList):
        self.task_list_dao.delete(task_list.ID)
        self.all_lists.remove(task_list)


    def login(self):
        pass

    def logout(self):
        pass

    def register(self):
        pass
