import tkinter as tk
from tkinter import ttk

from themes.main_themes import *

class MainMenu(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        content = tk.Frame(self)
        content.place(relx=0.5, y=20, anchor="n")
        content.configure(bg=BACKGROUND_COLOR)

        button_width = 20
        self.configure(bg=BACKGROUND_COLOR)

        style = ttk.Style(self)
        style.theme_use("default")

        style.configure(
            "Menu.TButton",
            font=BUTTON_FONT,
            padding=10,
            background=BUTTON_COLOR
        )

        style.map(
            "Menu.TButton",
            background=[("active", ACTIVE_BUTTON_COLOR)]
        )

        menuTitle = tk.Label(
                content, 
                text="Main Menu", 
                font=TITLE_FONT,
                background=BACKGROUND_COLOR,
                fg="white")
        menuTitle.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        buttons = [
            ("Program", "Program"),
            ("Select Message", "SelectMsg"),
            ("View Recordings", "ViewRecordings"),
            ("Status Report", "StatusReport"),
            ("System Reboot", None),
            ("Control", "Control")
        ]

        # Create buttons in a grid
        for i, (text, frame_name) in enumerate(buttons):
                if frame_name:
                        action = lambda fn=frame_name: app.show_frame(fn)
                else:
                        action = None  # Placeholder for System Reboot or other actions
        
                ttk.Button(
                        content,
                        text=text,
                        style="Menu.TButton",
                        width=button_width,
                        command=action
                ).grid(row=1 + i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")


