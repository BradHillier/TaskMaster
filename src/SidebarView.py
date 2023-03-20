import tkinter 
import customtkinter

class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = customtkinter.CTkButton(master=self,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         text="Create List")
        self.button.grid(row=0, column=0, pady=(10, 40), padx=10, sticky="nwe")

        self.button2 = customtkinter.CTkButton(master=self,
                                         fg_color='transparent',
                                         text_color_disabled='#1f6ba5',
                                         corner_radius=0,
                                         text="List Name",
                                         state="disabled")
        self.button2.grid(row=1, column=0, sticky="nwe")

        self.list_item = tkinter.StringVar(value="Todo List")
        self.label = customtkinter.CTkLabel(master=self, textvariable=self.list_item)
        self.label.grid(row=2, column=0,  padx=60, pady=20, sticky="nsw")
