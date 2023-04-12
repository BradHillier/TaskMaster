import sys

sys.path.insert(1, '../Model')
sys.path.insert(1, '../View')
from TaskMaster import TaskMaster
from TaskMasterView import App
from Task import Task


class Controller:

    def __init__(self):
        self.model = TaskMaster()
        self.view = App()

    def retreiveTaskView(self, task: Task):
        raise NotImplemented

    def switchTaskList(self, list_index: int):
        raise NotImplemented

