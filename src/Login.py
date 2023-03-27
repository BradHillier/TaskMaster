import tkinter 
import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk


class LoginPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        master.title("Login")

        # allows the input box to expand with the window
        self.grid_columnconfigure(1, weight=1)

        # adds hidden rows before and after content which help to keep
        # the form centered in the window
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.username_CTkLabel = ctk.CTkLabel(self, text="Username")
        self.username_CTkLabel.grid(row=1, column=0, padx=10, pady=5)

        self.username_entry = ctk.CTkEntry(self)
        # sticky='nsew' allows the entry to take up it's entire grid cell
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky='nsew') 

        self.password_CTkLabel = ctk.CTkLabel(self, text="Password")
        self.password_CTkLabel.grid(row=2, column=0, padx=10, pady=5)

        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login successful!")

            # the windowing being hidden is currently the trigger for switching 
            # to the logged in view
            self.grid_remove()
        else:
            messagebox.showerror("Login", "Incorrect username or password")

    def register(self):
        register_window = ctk.CTkToplevel(self.master)
        register_window.grid_rowconfigure(0, weight=1)
        register_window.grid_columnconfigure(0, weight=1)
        register_page = RegisterPage(register_window, fg_color='transparent')
        register_page.grid(row=0, column=0, padx=100, pady=100, sticky='nsew')

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        master.title("Register")

        # allows the input box to expand with the window
        self.grid_columnconfigure(1, weight=1)

        # adds hidden rows before and after content which help to keep
        # the form centered in the window
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.username_CTkLabel = ctk.CTkLabel(self, text="Username")
        self.username_CTkLabel.grid(row=1, column=0, padx=10, pady=5)

        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')

        self.password_CTkLabel = ctk.CTkLabel(self, text="Password")
        self.password_CTkLabel.grid(row=2, column=0, padx=10, pady=5)

        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

        self.confirm_password_CTkLabel = ctk.CTkLabel(self, text="Confirm Password")
        self.confirm_password_CTkLabel.grid(row=3, column=0, padx=10, pady=5)

        self.confirm_password_entry = ctk.CTkEntry(self, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if username == "":
            messagebox.showerror("Register", "Please enter a username")
        elif password == "":
            messagebox.showerror("Register", "Please enter a password")
        elif password != confirm_password:
            messagebox.showerror("Register", "Passwords do not match")
        else:
            messagebox.showinfo("Register", "Registration successful!")
            self.master.destroy()


if __name__ == '__main__':
    root = ctk.CTk()

    # allows the widget place in row 0 and column 0 to expand 
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # fg_transparent hides the default frame background colour
    login_page = LoginPage(master=root, fg_color='transparent')
    login_page.grid(row=0, column=0, sticky='nsew')
    root.mainloop()
