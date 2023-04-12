import tkinter
import customtkinter
from TaskScrollerView import TaskScrollerView
from AddTask import AddTask

class ListContentView(customtkinter.CTkFrame):
    '''
    composed of the list's title and column headers above a scrolling
    collection of task of the lists
    '''

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure(1, weight=1)

        #=====================================================================
        # This is intended to contain all variables for fine tuning the
        # List Contents UI, including its sub widegets
        #=====================================================================
        # adjust the horizontal space before content
        # this could have been done using the padx property when placing
        # this widget in a grid, but this would cause the scroller bar 
        # to also contain padding
        self.margin = 70    
        self.padding = 40

        self.header_pady = 0
        self.header_padx = 10
        self.list_name_font = customtkinter.CTkFont(family="Arial", size=36)

        self.task_height = 40
        #=====================================================================

        self.list_name = tkinter.StringVar(value="Chores")
        self.due_header = tkinter.StringVar(value="Due")
        self.priority_header = tkinter.StringVar(value="Priority")

        self._createListTitle()
        self._createHeader()
        self._createTaskList()

        self._create_add_task_button()

    def _create_add_task_button(self):
        btn_plus = tkinter.StringVar(value="+")
        self.plus_button = customtkinter.CTkButton(master=self, textvariable=btn_plus, width=48, font=self.list_name_font, corner_radius=48)
        self.plus_button.grid(row=1, column=3, padx=18, pady=18, sticky='se')

    def _createListTitle(self):
        self.label = customtkinter.CTkLabel(self, 
                            textvariable=self.list_name,
                            font=self.list_name_font)
        self.label.grid(
                    row=0, column=0, 
                    columnspan=2, 
                    padx = self.margin + self.header_padx, 
                    pady=self.header_pady, 
                    sticky="nsw")

    def _createHeader(self):

        # Create and position the due date header
        self.label = customtkinter.CTkLabel(
                master = self,
                textvariable = self.due_header)
        self.label.grid(
                row = 0,
                column = 2,
                padx = (0, self.task_height + 20),
                sticky = "se")

        # Create and position the priority header
        self.label = customtkinter.CTkLabel(
                master = self,
                textvariable = self.priority_header)
        self.label.grid(
                row = 0,
                column = 3,
                padx = (0, self.margin + self.task_height / 2),
                sticky = "se")

    def _createTaskList(self):
        self.task_scroller = TaskScrollerView(
                master = self, 
                task_size = self.task_height,
                margin = self.margin, 
                fg_color = 'transparent')
        self.task_scroller.grid(
                row=1,
                column=0,
                columnspan=4, # use the entirety of the grids horizontal space
                sticky='nsew')

    def open_edit_task_page(self):
        new_task_window = customtkinter.CTkToplevel(self.master)
        new_task_window.title("New Task")
        new_task_page = AddTask(new_task_window, fg_color='transparent')
        new_task_page.pack(expand=True, fill='both')
        return new_task_page
