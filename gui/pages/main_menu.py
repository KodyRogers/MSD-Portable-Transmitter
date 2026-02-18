import tkinter as tk
from tkinter import ttk

from gui.pages.themes.main_themes import *

class MainMenu(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        content = tk.Frame(self, bg=BACKGROUND_COLOR)
        content.place(relx=0.5, y=20, anchor="n")

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

        # ---- TITLE ----
        menuTitle = tk.Label(
            content,
            text="Main Menu",
            font=TITLE_FONT,
            background=BACKGROUND_COLOR,
            fg="white"
        )
        menuTitle.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # ---- MENU BUTTONS ----
        buttons = [
            ("Program", "Program"),
            ("Select Message", "SelectMsg"),
            ("View Recordings", "ViewRecordings"),
            ("Status Report", "StatusReport"),
            ("System Reboot", None),
            ("Control", "Control")
        ]

        lastrow = 0
        
        for i, (text, frame_name) in enumerate(buttons):
            if frame_name:
                action = lambda fn=frame_name: app.show_frame(fn)
            else:
                action = None  # placeholder

            ttk.Button(
                content,
                text=text,
                style="Menu.TButton",
                width=button_width,
                command=action
            ).grid(
                row=1 + i // 2,
                column=i % 2,
                padx=10,
                pady=10,
                sticky="nsew"
            )
            lastrow = i

        self.recording_label = tk.Label(
            content,
            font = SUBTITLE_FONT,
            text = "Start / Stop Recording",
            background=BACKGROUND_COLOR,
            fg = "white"
        )
        self.recording_label.grid(
            row=lastrow,
            column=0,
            columnspan=2,
            pady=(20,5)
        )
    # ---- START / STOP BUTTON ----
        self.start_stop_btn = ttk.Button(
            content,
            text="Start",
            style="Menu.TButton",
            width=button_width,
            command=self.toggle
        )
        self.start_stop_btn.grid(row=lastrow+1, column=0, columnspan=2, pady=10)
    
    # ---------- START / STOP ----------
    def toggle(self):
        self.app.toggle()
        self.update_button()

    def update_button(self):
        self.start_stop_btn.config(
            text="Stop" if self.app.running else "Start"
    )

    def start_clock_updates(self):
        # This function calls itself every second
        self.app.clock.update()  # <-- update HT16K33 display
        self.start_stop_btn.after(1000, self.start_clock_updates)

    def tkraise(self):
        super().tkraise()
        self.update_button()
        
        if not hasattr(self, "_clock_updating"):
            self._clock_updating = True
            self.start_clock_updates()
