import tkinter 
import customtkinter
from functools import partial


class TaskListNavButton(customtkinter.CTkFrame):
    '''
    A sidebar button used to switch between list views

    The widget has two states: normal and text entry

    In the **normal** state, a button is visible with a transparent background.
    When moused over, the buttons background will change to the widget's 
    highlight color and the text will turn white.  As the mouse leaves the 
    button, the colors will change back to their default values.

    In the **text entry** state, a text entry appears over top of the button,
    hiding it from view. Upon appearing, the text entry will contain the 
    text from the buttons label. The entry will be shown in two distinct case.

    1. The button is double clicked
    2. The widget is created with out a title

    The text entry state can be exited with out saving by pressing 
    <kbd>ESC</kbd> or clicking outside of the entry. The state of the entry can
    be saved by pressing <kbd>ENTER</kbd>
    '''

    def __init__(self, master, title: str=None, **kwargs):
        '''
        TaskListMenuButton's initial state is dependant on 
        If a title is provided on creation, it will start with the
        button visible. Otherwise, it will start with the entry visible
        allowing the user to enter a name

        :param title: the text to be used as the buttons label
        '''
        super().__init__(master, **kwargs)

        self.highlight_color: str = '#1F6AA5'
        '''
        the default foreground color for button text and background
        color when mouse over

        can be a word like ```'white', 'red'```, etc or an hex RGB value such as ```'#FFFFFF', '#FF0000'```, etc

       for more information, view [Tkinter Colors - A Complete Guide](https://www.askpython.com/python-modules/tkinter/tkinter-colors)
        '''

        self.button: customtkinter.CTkButton = self._create_button()
        '''
        The button is used to switch between different views of task lists. 

        * allows the user to switch between different views of task lists
        * double-click to rename a task and display text entry
        * highlights when the mouse hovers over it
        '''

        self.entry: customtkinter.CTkEntry = self._create_entry()
        '''
        used for naming newly created task lists and renaming existing ones

        * press ESC to exit without saving changes
        * press ENTER to commit changes

        '''

        if title:
            self.button.configure(text=title)
            self.button.grid()
        else:
            self.display_entry()

    def display_entry(self, event: tkinter.Event = None):
        '''
        Display the text entry for renaming the task list and focus on it

        :param event: Automatically passed to the method when invoked from a bind event being triggered
        '''
        self.entry.insert(0, self.button.cget('text'))
        self.entry.grid(row=0, column=0)
        self.entry.focus()

    def hide_entry(self, event: tkinter.Event = None):
        '''
        Hide the text entry used for renaming the task list

        :param event: Automatically passed to the method when invoked from a bind event being triggered
        '''
        self.entry.grid_remove()
        self.entry.delete(0, 'end')

    def _create_button(self) -> customtkinter.CTkButton:
        '''
        Creates the button that is used to switch from one task list view
        to another. Double clicking on the button opens an entry for
        modifying the task list's name.
        '''
        button = customtkinter.CTkButton(
                master=self,
                fg_color='transparent',
                text_color=self.highlight_color,
                text_color_disabled='green',
                corner_radius=0,
                text=' ')   # allows button to initialize before entry

        # partial is used to pass objects from the current scope as arguments
        button.bind('<Button-1>', partial(self.master.select_list, button))

        # display entry form for renaming the task list when double clicked
        button.bind('<Double-Button-1>', self.display_entry)       

        # highlight the background when moused over
        button.bind("<Enter>", self._highlight_button)

        # return to normal when mouse leaves
        button.bind("<Leave>", self._reset_button_style)

        button.grid(row=0, column=0)
        return button

    def _create_entry(self) -> customtkinter.CTkEntry:
        '''
        Creates a text entry input used for renaming the task list
        '''
        entry = customtkinter.CTkEntry(master=self)

        # hide the text entry when focusing on another widget or pressing <Esc>
        entry.bind("<Escape>", self.hide_entry)
        entry.bind("<FocusOut>", self.hide_entry)

        # update the task list's name to the contents of the text entry
        # when return is pressed
        entry.bind("<Return>", self._update_button_text)
        return entry

    
    def _update_button_text(self, event: tkinter.Event = None):

        # TODO: a call to the controller to adjust the model 

        new_text = self.entry.get()
        self.button.configure(text=new_text)
        self.hide_entry()

    def _highlight_button(self, event: tkinter.Event = None):
        '''
        highlight the background of the button and set foreground to white
        '''
        if self.button.cget('state') != 'disabled':
            self.button.configure(
                    text_color = 'white', 
                    bg_color = self.highlight_color)

    def _reset_button_style(self, event: tkinter.Event = None):
        self.button.configure(
                text_color = self.highlight_color,
                bg_color = 'transparent')





class SideBar(customtkinter.CTkFrame):

    selected = None
    task_lists = []

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.make_create_list_button()

        # Create task list buttons for each title
        task_list_titles = ['inbox', 'today', 'upcoming', 'all']
        for title in task_list_titles:
            self.task_lists.append(
                    TaskListNavButton(self, title, fg_color='transparent'))

        # Place the task list buttons within the side bar in current order
        for idx, task_list in enumerate(self.task_lists):
            task_list.grid(row=self.grid_size()[1], column=0)

    def make_create_list_button(self) -> customtkinter.CTkButton:
        ''' 
        A button for creating a new task list. When clicked, an entry
        will appear allowing the user to enter a name for their new list
        '''
        self.button = customtkinter.CTkButton(
                master=self,
                width=120,
                height=32,
                border_width=0,
                corner_radius=8,
                text="Create List",
                command=self.add_task_list)
        self.button.grid(row=0, column=0, pady=(10, 40), padx=20, sticky="nwe")
        self.button.focus()

    def select_list(self, widget, event=None):

        # reset the currently selected button
        if self.selected != None:
            self.selected.configure(state='normal')
        # set the newly selected button
        widget.configure(state='disabled', bg_color='transparent', text_color='#1F6AA5')
        self.selected = widget

    def add_task_list(self):
        new_task_list = TaskListNavButton(self, fg_color='transparent')
        new_task_list.grid(row=self.grid_size()[1], column=0)
