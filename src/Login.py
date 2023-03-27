import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.username_label = tk.Label(master, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Incorrect username or password")

    def register(self):
        register_window = tk.Toplevel(self.master)
        register_page = RegisterPage(register_window)

class RegisterPage:
    def __init__(self, master):
        self.master = master
        master.title("Register")

        self.username_label = tk.Label(master, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.confirm_password_label = tk.Label(master, text="Confirm Password")
        self.confirm_password_label.pack()

        self.confirm_password_entry = tk.Entry(master, show="*")
        self.confirm_password_entry.pack()

        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Register", "Passwords do not match")
        else:
            messagebox.showinfo("Register", "Account created successfully!")
            self.master.destroy()

root = tk.Tk()
login_page = LoginPage(root)
root.mainloop()
