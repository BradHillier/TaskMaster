#!../bin/python3.9

import tkinter 
import customtkinter

from src.View.ListContentView import ListContentView
from src.View.SidebarView import SideBar
from src.View.TopbarView import TopBar
from src.View.Login import LoginPage
from src.Model.TaskMaster import TaskMaster


class TaskMasterView(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # allow side bar and list view to expand vertically with the window
        self.grid_rowconfigure(1, weight=1)

        # allow the top bar and list view to expand horizontally with the window
        self.grid_columnconfigure(1, weight=1)

        # create and position the top bar
        self.top_bar = TopBar(self, border_width=1, corner_radius=0)
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky="nwe")

        # create and position the side bar
        self.side_bar = SideBar(master=self, corner_radius=0)
        self.side_bar.grid(row=1, column=0, sticky="nsw");

        # create and position the list view which contains a header and 
        # a scrollable collection of tasks
        self.list_view_frame = ListContentView(master=self, fg_color="transparent")
        self.list_view_frame.grid(row=1, column=1, pady=(40, 0), sticky="nsew");


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title('TaskMaster')
        
        self.minsize(500, 300)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.login = LoginPage(master=self, fg_color='transparent')
        self.login.grid(sticky='nsew')

        # when the login page is hidden, show the main view
        self.login.bind('<Unmap>', self.show_main_view)

        self.task_master = TaskMasterView(self, fg_color='transparent')
        self.task_master.bind('<Unmap>', self.show_login_view)

        # allows task list buttons text entry to hide when clicking outside it
        self.bind('<Button-1>', lambda event : event.widget.focus())

    def show_main_view(self, event):
        self.geometry('1000x600')
        self.task_master.grid(sticky='nsew')

    def show_login_view(self, event):
        self.geometry('500x300')
        self.login.grid(sticky='nsew')

if __name__ == '__main__':
    task_master = App()
    task_master.mainloop()
