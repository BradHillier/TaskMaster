import tkinter
import customtkinter as ctk
from tkinter import messagebox

# from tkinter import *
from tkinter import Text
from tkcalendar import Calendar

class AddTask(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        master.title("New Task")

        # set this size as it looks the most natural with little white space
        self.master.geometry("500x400")

        self.master.minsize(width=400, height=400) # anything smaller and the calendar gets too small 
        
        # Grid configuration 
        self.grid_columnconfigure(0, weight=2) # empty columnm
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=2) # empty column

        # to center everything vertically
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(8, weight=1)


        # Task Name Label
        self.task_name_label = ctk.CTkLabel(self, text="Task Name:")
        self.task_name_label.grid(row=1, column=1, padx=10, pady=5)

        # Task Name Input
        self.task_name_entry = ctk.CTkEntry(self)
        self.task_name_entry.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky='nsew')

        # Task Desc
        self.task_desc_label = ctk.CTkLabel(self, text="Description:")
        self.task_desc_label.grid(row=2, column=1, padx=10, pady=5)

        # Task Desc Input
        self.task_desc_text = Text(self, height=2)
        self.task_desc_text.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky='nsew')

        # Due Date Label
        self.due_date_label = ctk.CTkLabel(self, text="Due Date:")
        self.due_date_label.grid(row=4, column=1, padx=10, pady=5)

        # Date Picker
        self.due_date_picker = Calendar(self, showweeknumbers=False, weekendbackground='white', weekendforeground='black')
        self.due_date_picker.grid(row=5, column=1, columnspan=2, rowspan=3, padx=10, pady=5, sticky='nsew')

        # Priority Label
        self.priority_label = ctk.CTkLabel(self, text="Priority:")
        self.priority_label.grid(row=5, column=3, padx=10, pady=5)

        # Priority Combo
        self.priority_combobox = ctk.CTkComboBox(master=self, values=["Low", "Medium", "High"], state="readonly")
        self.priority_combobox.grid(row=6, column=3, padx=20, pady=20, sticky="ew")

        # Create Task button
        self.button = ctk.CTkButton(master=self, command=self.submit_task, text="Create Task")
        self.button.grid(row=7, column=3, padx=20, pady=20, sticky="ew")


    # TODO in the future will need to process / pass this data to the db and create a task object
    def submit_task(self):
        task_name = self.task_name_entry.get()
        task_desc = self.task_desc_text.get("1.0", "end-1c")
        due_date = self.due_date_picker.get_date()
        priority = self.priority_combobox.get()

        if not task_name:
            messagebox.showerror("Task Name", "Please enter a task name")
        elif not task_desc:
            messagebox.showinfo("Task", "No description given")
        elif not due_date:
            messagebox.showerror("Task", "No Date?") # I don't think this will ever be the case since defualt date will be today
        elif not priority:
            messagebox.showerror("Task", "No priority")
        else:
            messagebox.showinfo("New Task Details", f"Name: {task_name}\n \
                                                      Desc: {task_desc}\n \
                                                      Date: {due_date} \n \
                                                      Priority: {priority}" \
                                                      )
            self.master.destroy()
