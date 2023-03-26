import tkinter 
import customtkinter
from functools import partial

class SideBar(customtkinter.CTkFrame):

    selected = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.count = 0

        self.add_create_list_button()

        todo_lists = ['inbox', 'today', 'upcoming', 'all']
        self.todo_lists = [self.create_list(title) for title in todo_lists]

        self.select_list(self.todo_lists[0])

    def add_create_list_button(self):
        self.button = customtkinter.CTkButton(master=self,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         text="Create List")
        self.button.grid(row=self.count, column=0, pady=(10, 40), padx=20, sticky="nwe")
        self.count += 1

    def create_list(self, title) -> customtkinter.CTkButton:
        button = customtkinter.CTkButton(master=self,
                                         fg_color='transparent',
                                         text_color='#1F6AA5',
                                         text_color_disabled='green',
                                         corner_radius=0,
                                         text=title)
        # partial is used to pass objects from the current scope as arguments
        button.bind('<Button-1>', 
                    partial(self.select_list, button))
        button.bind('<Double-Button-1>', 
                    partial(self.update_name, button))
        button.bind("<Enter>", 
                    partial(color_config, button, "#FFFFFF", '#1F6AA5'))
        button.bind("<Leave>", 
                    partial(color_config, button, "#1F6AA5", 'transparent'))
        button.grid(row=self.count, column=0, )
        self.count += 1
        return button

    def select_list(self, widget, event=None):

        # reset the currently selected button
        if self.selected != None:
            self.selected.configure(state='normal')
        # set the newly selected button
        widget.configure(state='disabled', bg_color='transparent', text_color='#1F6AA5')
        self.selected = widget

    def update_name(self, widget, event=None):
        entry = customtkinter.CTkEntry(master=self, placeholder_text=widget.cget('text')) 
        entry.insert(0, widget.cget('text'))

        entry.bind("<Escape>", partial(delete, entry))
        entry.bind("<FocusOut>", partial(delete, entry))
        entry.bind("<Return>", partial(update, entry, widget))

        # place overtop of the passed widget
        row = widget.grid_info()['row']
        column = widget.grid_info()['column']
        entry.grid(row=row, column=column)
        entry.focus()

def delete(widget, event):
    widget.destroy()

def update(entry, widget, event):
    widget.configure(text=entry.get())
    entry.destroy()

def color_config(widget, fg, bg, event):
    if widget.cget('state') != 'disabled':
        widget.configure(text_color=fg, bg_color=bg)
