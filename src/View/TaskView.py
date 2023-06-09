import tkinter
import customtkinter
from datetime import date, datetime, timedelta
from tkinter import ttk
from tkinter import messagebox
import emoji

# this code heavily relies on tkinters grid positioning system
# this system allows easy specification of how widgets move around when the 
# window is resized

# the sticky property when setting a widgets position within it's masters grid
# controls which section the widget will anchor to
#
# i.e "se" will anchor a widget in the cells south east (bottom right) corner


class TaskView(customtkinter.CTkFrame):
    '''
    takes up the entire width of its master and padding * 2 vertical space
    '''

    def __init__(self, master, ID: int, name: str, date: date, priority: str, isCompleted: bool , **kwargs):
        super().__init__(master, **kwargs)

        self.padding = self.cget('height') / 2
        self.grid_columnconfigure(1, weight=1)

        self.ID = ID

        # The UI will automatically update if the value of any of the below
        # StringVar's change
        if isCompleted:
            self.checkbox_status = tkinter.StringVar(value="on")
        else:
            self.checkbox_status = tkinter.StringVar(value="off")

        self.task_name = tkinter.StringVar(value=name)

        days_till_due = (date - date.today()).days
        if days_till_due < 0:
            due_str = f'{abs(days_till_due)} days ago'
        else:
            due_str = f'{days_till_due} days left'
        self.date = tkinter.StringVar(value=due_str)
        priority_emoji = emoji.emojize(f'{priority}')
        self.priority = tkinter.StringVar(value=priority_emoji)

        self._create_checkbox()
        self._create_task_name()
        self._create_due_date()
        self._create_priority()
        self._create_buttons()

    def update(self, **kwargs):
        if 'isCompleted' in kwargs:
            if kwargs.get('isCompleted'):
                self.checkbox_status.set("on")
            else:
                self.checkbox_status.set("off")

        if 'taskName' in kwargs:
            self.task_name.set(kwargs.get('taskName'))

        if 'dueDate' in kwargs:
            days_till_due = (kwargs.get('dueDate') - datetime.today()).days
            if days_till_due < 0:
                due_str = f'{abs(days_till_due)} days ago'
                self.date_label.configure(text_color='red')
            else:
                due_str = f'{days_till_due} days left'
                self.date_label.configure(text_color='white')
            self.date.set(due_str)
        if 'priority' in kwargs:
            priority_emoji = emoji.emojize(f'{kwargs.get("priority")}')
            self.priority.set(priority_emoji)



    def _create_buttons(self):
        edit_icon = "✎"
        trash_icon = "🗑"

        # Set the font for the icons
        #icon_font = Font(size=24)

        style = ttk.Style()
        style.configure('Icon.TButton', padding=(2, 0))

        self.edit_button = customtkinter.CTkButton(
                master=self,
                text=edit_icon,
                command=self.edit_button_event,
                font=('Arial', 24),
                width=5
        )
        self.edit_button.grid(row=0, column=5, padx=(5), sticky="w")

        self.trash_button = customtkinter.CTkButton(
                master=self,
                text=trash_icon,
                font=('Arial', 24),
                width=5
        )
        self.trash_button.grid(row=0, column=5, padx=(50,5), sticky="e")

    def edit_button_event(self):
        pass

    def trash_button_event(self):
        pass

    def _create_checkbox(self):
        '''
        Creates a checkbox widget and adds it to the task widget. The widget 
        is divided into a grid with 1 row and 4 columns, one for each of the
        tasks sub widgets (a checkbox and three labels).

        the checkbox has an associated string variable which contains
        it's state, either 'on' or 'off'. When toggled, the checkbox_event
        method will be triggered. 
        '''
        # create a check box widget
        self.checkbox = customtkinter.CTkCheckBox(
                master = self,
                # text was intentionally left empty to allow better control of
                # the position of the task name using a label widget. If this
                # is removed, the text will default to CTkCheckbox
                text='', 
                command = self.checkbox_event,
                variable = self.checkbox_status,
                onvalue = 'on', offvalue = 'off')

        # place the newly created widget in the tasks grid
        self.checkbox.grid(
                row = 0, 
                column = 0, 
                padx = self.padding,          # add space between left edge of task and checkbox
                pady = self.cget('height')/2, # sets the height of the entire task widget
                sticky = 'w')                 # anchor checkbox to west side of grid cell

    def _create_task_name(self):
        task_name_label = customtkinter.CTkLabel(
                master = self, 
                textvariable = self.task_name)
        task_name_label.grid(
                row = 0, 
                column = 1, 
                sticky = 'w')

    def _create_due_date(self):
        self.date_label = customtkinter.CTkLabel(
                master = self, 
                textvariable = self.date)
        if 'ago' in self.date.get():
            self.date_label.configure(text_color='red')
        self.date_label.grid(
                row = 0, 
                column = 2, 
                # adds space between priority and due date
                padx = self.padding * 3, 
                sticky = 'e')

    def _create_priority(self):
        priority_label = customtkinter.CTkLabel(
                master = self,
                textvariable = self.priority)
        priority_label.grid(
                row = 0, 
                column = 3, 
                padx = self.padding,
                sticky = 'e')

    def checkbox_event(self):
        if self.checkbox_status.get() == 'on':
            # do something when the box is checked
            pass
        else:
            # do something else when the box is unchecked
            pass

