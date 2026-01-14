import tkinter as tk

class SystemReboot(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        tk.Label(self, text="System Reboot Page", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Back to Main Menu",
                  command=lambda: app.show_frame("MainMenu")).pack(pady=5)