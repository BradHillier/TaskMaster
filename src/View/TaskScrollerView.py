import customtkinter
from src.View.TaskView import TaskView


class TaskScrollerView(customtkinter.CTkScrollableFrame):

    def __init__(self, master, margin=20, task_size=40, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.task_views = []

    def clear(self):
        for task in self.task_views:
            task.destroy()
        self.task_views.clear()
