import tkinter 
import customtkinter

class TopBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # adds padding between left and right side of the bar
        self.grid_columnconfigure(1, weight=1) 
        
        # Application title
        self.list_item = tkinter.StringVar(value="Task Master")
        font=customtkinter.CTkFont(family="Monospace", size=24)
        self.label = customtkinter.CTkLabel(master=self, textvariable=self.list_item, font=font)
        self.label.grid(row=0, column=0,  padx=60, pady=20, sticky="nsw")

        # Welcome Message
        self.welcome_message = tkinter.StringVar(value="Welcome <User Name>")
        self.welcome_label = customtkinter.CTkLabel(master=self, textvariable=self.welcome_message)
        self.welcome_label.grid(row=0, column=2,  padx=60, pady=20, sticky="nse")

        # Logout Button
        self.button = customtkinter.CTkButton(master=self,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         command=self.logout,
                                         text="Logout")
        self.button.grid(row=0, column=3, pady=10, padx=10, sticky="e")

    def logout(self):
        self.master.grid_remove()

