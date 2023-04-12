import sys
import dateparser
from functools import partial

sys.path.insert(1, '../Model')
from TaskMaster import TaskMaster
from Task import Task

sys.path.insert(1, '../View')
from TaskView import TaskView
from TaskMasterView import App
from AddTask import AddTask


class Controller:

    def __init__(self):
        self.model = TaskMaster()
        self.view = App()
        self.switchTaskList(0)
    
        # add event bindings for renaming and selecting a task list
        for task_list in self.model.all_lists:
            sidebar = self.view.task_master.side_bar
            sidebar.add_task_list(task_list.name)
            list_idx = len(sidebar.task_lists) - 1

            # switch the task list view when clicking on the newly created list
            new_list_button = sidebar.task_lists[-1].button
            new_list_entry = sidebar.task_lists[-1].entry
            new_list_button.bind(
                    '<Button-1>', partial(self.switchTaskList, list_idx))
            new_list_entry.bind(
                    '<Return>', partial(self.renameTaskList, list_idx))

        add_task_btn = self.view.task_master.list_view_frame.plus_button
        add_task_btn.bind( '<Button-1>', self.createTaskInput)


            
        # This has to be the last thing in __init__
        self.view.mainloop() 

    def retreiveTaskView(self, task: Task):
        """Create a TaskView using the provided Task and place it in the UI
        
        :param task: A Task model containing data to be displayed 
        """
        list_content = self.view.task_master.list_view_frame

        # Create a TaskView from the provided Task model
        task = TaskView(
                master = list_content.task_scroller,
                ID = task.ID,
                name = task.name,
                date = dateparser.parse(task.dueDate),
                priority = task.priority,
                isCompleted = task.isCompleted,
                height = 40)

        # Place the task in the list content view's task scroller
        task.grid(
                row = len(list_content.task_scroller.task_views), 
                column = 0, 
                padx = list_content.margin,
                pady = 11,
                sticky='ew')
        list_content.task_scroller.task_views.append(task)

    def switchTaskList(self, list_index: int, event=None):
        list_view = self.view.task_master.list_view_frame

        # empty out the old tasks
        list_view.task_scroller.clear()

        # update model and re-render the list view's scroller
        self.model.changeList(self.model.all_lists[list_index])
        for task in self.model.current_list:
            self.retreiveTaskView(task)

        # set the list view heading name to the new list's name
        list_view.list_name.set(self.model.current_list.name)

    def renameTaskList(self, list_index: int, event=None): 
        name = self.view.task_master.side_bar.task_lists[list_index].button.cget('text')
        self.model.renameList(self.model.all_lists[list_index], name)

        # update the list view header if the renamed list is the selected list
        if self.model.all_lists[list_index] == self.model.current_list:
            list_view = self.view.task_master.list_view_frame
            list_view.list_name.set(self.model.current_list.name)

    def createTaskInput(self, event):
        edit_window = self.view.task_master.list_view_frame.open_edit_task_page()
        edit_window.button.bind(
                '<Button-1>', partial(self.processTaskInputs, edit_window))

    def processTaskInputs(self, widget, event):
        keywords = {
                'listID':  self.model.current_list.ID,
                'username': self.model.user.username,
                'taskName':  widget.task_name_entry.get(),
                'description': widget.task_desc_text.get("1.0", "end-1c"),
                'dueDate': dateparser.parse(widget.due_date_picker.get_date()),
                'isCompleted': False,
                'priority': widget.priority_combobox.get()
            }
        self.model.createTask(**keywords)
        self.retreiveTaskView(self.model.current_list[-1])
        widget.master.destroy()

if __name__ == '__main__':
    myContrller = Controller()
