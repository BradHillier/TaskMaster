import customtkinter
from TaskView import TaskView


class TaskScrollerView(customtkinter.CTkScrollableFrame):

    def __init__(self, master, margin=20, task_size=40, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        distance_between_tasks = 10

        tasks = [
            'Washing bedding',
            'Taking out the trash',
            'Wash the car',
            'Washing windows',
            'Bathing pets',
            'Clean refrigerator',
            'Change air filters on a furnace or air conditioner',
            'Dry and put away dishes',
            'Put groceries away',
            'Organize pantry',
            'Make the bed',
            'Put books away on shelves',
            'Hang and fold clean clothes',
            'Wipe out bathroom cupboard',
            'Prepare snacks',
            'Prepare simple meal',
            'Water outdoor plants',
            'Weed garden',
            'Hose off patio',
            'Change light bulbs']

        for i, task in enumerate(tasks):
            self.my_frame = TaskView(
                    master=self, 
                    name=task,
                    height=task_size)
            self.my_frame.grid(
                    row = i, 
                    column = 0, 
                    padx = margin,
                    pady = distance_between_tasks,
                    sticky='ew')

