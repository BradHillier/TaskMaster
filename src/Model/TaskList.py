from User import User
from Task import Task


class TaskList(list):

    def __init__(self, ID: int, name: str, user: User):
        super().__init__()
        self.ID: int = ID
        self.name: str = name
        self.user: str = user

    def __eq__(self, other_list):
        return self.ID == other_list.ID

    def __add__(self, other_list):
        for item in other_list:
            self._typeCheck(item)
        super().__add__(other_list)

    def append(self, item):
        self._typeCheck(item)
        super().append(item)

    def extend(self, other_list):
        for item in other_list:
            self._typeCheck(item)
            super().append(item)

    def _typeCheck(self, item):
        if not isinstance(item, Task):
            raise TypeError(f'Invalid {type(item)} cannot be added to TaskList')

    def __repr__(self):
        return f'Task(ID={self.ID}, name={self.name}, user={self.user}, tasks={[task.name for task in self]})'
