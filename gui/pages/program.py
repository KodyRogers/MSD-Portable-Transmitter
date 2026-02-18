import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

from gui.pages.themes.main_themes import *

class Program(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent)
        my_font = SUBTITLE_FONT

        container_style = ttk.Style(self)
        container_style.configure("TFrame", background=BACKGROUND_COLOR)

        container = ttk.Frame(self, style="TFrame")
        container.pack(fill="both", expand=True)

        content = tk.Frame(container)
        content.grid(row=0, column=0, sticky="nsew")
        content.place(relx=0.5, y=20, anchor="n")
        content.configure(bg=BACKGROUND_COLOR)

        bottom_bar = tk.Frame(container)
        bottom_bar.grid(row=1, column=0, sticky="ew")
        bottom_bar.configure(bg=BACKGROUND_COLOR)

        # Make container expandable
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # Bottom bar layout
        bottom_bar.columnconfigure(0, weight=1)
        bottom_bar.columnconfigure(1, weight=1)

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

        tk.Label(
            content, 
            text="Delay Between Messages (ms):", 
            font=my_font,
            background=BACKGROUND_COLOR,
            fg="white"
        ).pack(pady=(10, 0))
        delay_entry = tk.Entry(content, font=my_font)
        delay_entry.pack(pady=5)

        tk.Label(
            content, 
            text="Start Delay (ms):", 
            font=my_font,
            background=BACKGROUND_COLOR,
            fg="white"
        ).pack(pady=(10, 0))
        start_delay_entry = tk.Entry(content, font=my_font)
        start_delay_entry.pack(pady=5)

        tk.Label(
            content, 
            text="Iterations:", 
            font=my_font,
            background=BACKGROUND_COLOR,
            fg="white"
        ).pack(pady=(10, 0))
        duration_entry = tk.Entry(content, font=my_font)
        duration_entry.pack(pady=5)

        btn = ttk.Button(
            bottom_bar,
            text="Back to Main Menu",
            style="Menu.TButton",
            width=button_width,
            command=lambda: app.show_frame("MainMenu")
        )
        btn.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        
        def save_values():
            try:
                duration = float(duration_entry.get())
                delay = float(delay_entry.get())
                start_delay = float(start_delay_entry.get())
                print(f"Saved values: duration={duration}, delay={delay}, start_delay={start_delay}")
                messagebox.showinfo("Saved", "Settings saved successfully!")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid numbers.")

        save_button = ttk.Button(
            bottom_bar, 
            text="Save", 
            command=save_values, 
            style="Menu.TButton",
            width=button_width
        )
        save_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
