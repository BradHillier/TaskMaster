import copy
from src.Model.TaskDAO import TaskDAO
from src.Model.TaskListDAO import TaskListDAO
from src.Model.userDAO import UserDAO

from src.Model.User import User
from src.Model.Task import Task
from src.Model.TaskList import TaskList

class TaskMaster:

    def __init__(self):
        self.user = User(username='test_user', email='user@example.com')
        self.database = 'database.sqlite3'

        # data access objects
        self.user_dao = UserDAO(self.database)
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


    def login(self, username: str, password: str) -> bool:
        """Log in the user with the specified username and password

        :param username: The username of the user
        :param password: The password of the user
        :return: True if the login was successful, False otherwise
        """
        user_data = self.user_dao.getUserWithPassword(username)
        if user_data is not None and user_data["password"] == password:
            self.user = User(username=user_data["username"], email=user_data["email"])
            # get all tasks if the user is verified in all_lists
            self.all_lists = self.task_list_dao.getAll(self.user.username)
            # setting curent list
            self.current_list = self.all_lists[0] if self.all_lists else None
            return True
        # user not fond
        return False 

    def logout(self):
        self.user = None
        self.all_lists = []
        self.current_list = None

    def register(self, username: str, password: str, email: str) -> bool:
        """Register a new user with the specified username, password, and email

        :param username: The username of the new user
        :param password: The password of the new user
        :param email: The email of the new user
        :return: True if the registration was successful, False otherwise
        """
        try:
            self.user_dao.create(username=username, password=password, email=email)
            return True
        except:
            return False
