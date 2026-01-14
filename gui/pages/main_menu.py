import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        
        content = tk.Frame(self)
        content.place(relx=0.5, y=20, anchor="n")

        button_font = ("Arial", 14)
        button_width = 20
        button_height = 1


        tk.Label(content, text="Main Menu", font=button_font).pack(pady=10)

        tk.Button(content, text="Program",
                font=button_font,
                width=button_width,
                height=button_height,
                command=lambda: app.show_frame("Program")).pack(padx=10, pady=5)

        tk.Button(content, text="Select Message",
                font=button_font,
                width=button_width,
                height=button_height,
                command=lambda: app.show_frame("SelectMsg")).pack(padx=10, pady=5)

        tk.Button(content, text="View Recordings",
                font=button_font,
                width=button_width,
                height=button_height,
                command=lambda: app.show_frame("ViewRecordings")).pack(pady=5)

        tk.Button(content, text="Status Report",
                font=button_font,
                width=button_width,
                height=button_height,
                command=lambda: app.show_frame("StatusReport")).pack(pady=5)

        tk.Button(content, text="System Reboot",
                font=button_font,
                width=button_width,
                height=button_height,
                command=lambda: app.show_frame("SystemReboot")).pack(pady=5)

        tk.Button(content, text="Control",
                font=button_font,
                width=button_width,
                height=button_height,
                command=lambda: app.show_frame("Control")).pack(pady=5)
