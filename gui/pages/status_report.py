import tkinter as tk

class StatusReport(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        tk.Label(self, text="Status Report Page", font=("Arial", 14)).pack(pady=10)
        
        # TODO when there is more backend functionality

        tk.Button(self, text="Back to Main Menu",
                  command=lambda: app.show_frame("MainMenu")).pack(pady=5)
