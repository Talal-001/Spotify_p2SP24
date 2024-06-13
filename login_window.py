import tkinter as tk
from tkinter import ttk, messagebox
import pygame
from admin import Admin

pygame.init()
pygame.mixer.init()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login to Spotify")
        self.root.geometry("400x400")

        self.admin = Admin(username="admin", password="adminpass")

        ttk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack(pady=5)

        ttk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        self.admin_button = ttk.Button(self.root, text="Admin Login", command=self.admin_login)
        self.admin_button.pack(pady=5)

        self.user_button = ttk.Button(self.root, text="User Login", command=self.user_login)
        self.user_button.pack(pady=5)

        self.exit_button = ttk.Button(self.root, text="exit", command=self.exit, style="TButton")
        self.exit_button.pack(pady=5)

    def admin_login(self):
        from admin_musicplayer import AdminmusicPlayer
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == self.admin.username and password == self.admin.password:
            main_root = tk.Tk()
            AdminmusicPlayer(main_root)
            self.root.destroy()
            main_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid admin credentials")

    def user_login(self):
        from user_musicplayer import UserMusicPlayer
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "1234":
            main_root = tk.Tk()
            UserMusicPlayer(main_root)
            self.root.destroy()
            main_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid user credentials")
    
    def exit(self):
        self.root.destroy()