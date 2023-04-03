from User import User
from Task import Task


class TaskList:

    def __init__(self, ID: int, name: str, user: User):
        self.ID: int = ID
        self.name: str = name
        self.user: User = user
        self.tasks: list[Task] = []

