import sys

sys.path.insert(1, '../Model')
sys.path.insert(1, '../View')
from TaskMaster import TaskMaster
from TaskMasterView import App
from TaskView import TaskView
from Task import Task


class Controller:

    def __init__(self):
        self.model = TaskMaster()
        self.view = App()
        self.switchTaskList(0)

        # This has to be the last thing in __init__
        self.view.mainloop() 

    def retreiveTaskView(self, task: Task):
        list_content = self.view.task_master.list_view_frame
        task = TaskView(
                master = list_content.task_scroller,
                ID = task.ID,
                name = task.name,
                date = task.dueDate,
                priority = task.priority,
                isCompleted = task.isCompleted,
                height = 40)
        task.grid(
                row = len(list_content.task_scroller.task_views), 
                column = 0, 
                padx = list_content.margin,
                pady = 11,
                sticky='ew')
        list_content.task_scroller.task_views.append(task)

    def switchTaskList(self, list_index: int):
        self.model.changeList(self.model.all_lists[list_index])
        for task in self.model.current_list:
            self.retreiveTaskView(task)


if __name__ == '__main__':
    myContrller = Controller()
