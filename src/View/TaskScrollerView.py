import customtkinter
from TaskView import TaskView


class TaskScrollerView(customtkinter.CTkScrollableFrame):

    def __init__(self, master, margin=20, task_size=40, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.distance_between_tasks = 11
        self.task_size = task_size
        self.margin = margin
        self.task_views = []

    def showTasks(self, task_list: list):

        for i, task in enumerate(task_list):
            task = TaskView(
                    master=self, 
                    ID=task.ID,
                    name=task.name,
                    date=task.dueDate,
                    priority=task.priority,
                    isCompleted=task.isCompleted,
                    height=self.task_size)
            task.grid(
                    row = i, 
                    column = 0, 
                    padx = self.margin,
                    pady = self.distance_between_tasks,
                    sticky='ew')
            self.task_views.append(task)

