import tkinter 
import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

def create_blue_theme(style):
    style.theme_create("blue", parent="alt", settings={
        "TCTkLabel": {"configure": {"foreground": "#FFFFFF"}},
        "TEntry": {"configure": {"foreground": "#000000"}},
        "TButton": {"configure": {"background": "#3366CC", "foreground": "#FFFFFF"}},
    })

class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        # Create a custom style object
        self.style = ttk.Style(master)
        self.style.theme_use("blue")

        self.username_CTkLabel = ctk.CTkLabel(master, text="Username")
        self.username_CTkLabel.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = ctk.CTkEntry(master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_CTkLabel = ctk.CTkLabel(master, text="Password")
        self.password_CTkLabel.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = ctk.CTkEntry(master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = ctk.CTkButton(master, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.register_button = ctk.CTkButton(master, text="Register", command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Incorrect username or password")

    def register(self):
        register_window = ctk.CTkToplevel(self.master)
        register_page = RegisterPage(register_window)

class RegisterPage:
    def __init__(self, master):
        self.master = master
        master.title("Register")

        # Create a custom style object
        self.style = ttk.Style(master)
        self.style.theme_use("blue")

        self.username_CTkLabel = ctk.CTkLabel(master, text="Username")
        self.username_CTkLabel.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = ctk.CTkEntry(master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_CTkLabel = ctk.CTkLabel(master, text="Password")
        self.password_CTkLabel.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = ctk.CTkEntry(master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.confirm_password_CTkLabel = ctk.CTkLabel(master, text="Confirm Password")
        self.confirm_password_CTkLabel.grid(row=2, column=0, padx=10, pady=5)

        self.confirm_password_entry = ctk.CTkEntry(master, show="*")
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

        self.register_button = ctk.CTkButton(master, text="Register", command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

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

root = ctk.CTk()

style = ttk.Style(root)
create_blue_theme(style)

login_page = LoginPage(root)
root.mainloop()