import tkinter 
import customtkinter
from ListContentView import ListContentView
from SidebarView import SideBar
from TopbarView import TopBar


class TaskMaster(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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

task_master = TaskMaster()
task_master.mainloop()