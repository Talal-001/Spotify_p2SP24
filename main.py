import tkinter as tk
from tkinter import ttk
from login_window import LoginWindow

root = tk.Tk()

style = ttk.Style()
style.configure("TButton", foreground="teal", background="white", font=("programme", 19))
player = LoginWindow(root)
root.mainloop()
