import tkinter
import customtkinter
from src.View.TaskScrollerView import TaskScrollerView
from src.View.AddTask import AddTask
from tkinter import messagebox


class SortButton(customtkinter.CTkFrame):

    def __init__(self, master, text, up_command, down_command, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color='transparent')
        self.label = self._createLabel(text)
        self.label.grid(column=0, padx=(0, 10))

        self.up_button = self._createUpButton(up_command)
        self.up_button.grid(row=0, column=1)

        self.down_button = self._createDownButton(down_command)
        self.down_button.grid(row=0, column=2)

    def _createLabel(self, text):
        label = customtkinter.CTkLabel(
                master=self,
                text=text)
        return label

    def _createUpButton(self, command):
        up_arrow = "\u25B2"
        up_button = self._createbutton()
        up_button.configure(text=up_arrow)
        up_button.configure(command=command)
        return up_button

    def _createDownButton(self, command):
        down_arrow = "\u25BC"
        down_button = self._createbutton()
        down_button.configure(text=down_arrow)
        down_button.configure(command=command)
        return down_button

    def _createbutton(self):
        return customtkinter.CTkButton(
                master=self,
                font=("Arial", 8),
                width=2,
                height=1)


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
        self.plus_button.grid(row=1, column=5, padx=18, pady=18, sticky='se')

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
        self.due_date = SortButton(self, 'dueDate', None, None)
        self.due_date.grid(row=0, column=4, sticky='se')

        self.priority = SortButton(self, 'priority', None, None)
        self.priority.grid(row=0, column=5, padx=(30, 200), sticky='se')


    def _createTaskList(self):
        self.task_scroller = TaskScrollerView(
                master = self, 
                task_size = self.task_height,
                margin = self.margin, 
                fg_color = 'transparent')
        self.task_scroller.grid(
                row=1,
                column=0,
                columnspan=8, # use the entirety of the grids horizontal space
                sticky='nsew')

    def open_edit_task_page(self):
        new_task_window = customtkinter.CTkToplevel(self.master)
        new_task_window.title("New Task")
        new_task_page = AddTask(new_task_window, fg_color='transparent')
        new_task_page.pack(expand=True, fill='both')
        return new_task_page

    def show_ascending_message(self):
        messagebox.showinfo("Info", "Ascending")

    def show_descending_message(self):
        messagebox.showinfo("Info", "Descending")
