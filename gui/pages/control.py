import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox

from gui.pages.themes.main_themes import *

class Control(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.configure(bg=BACKGROUND_COLOR)
        style = ttk.Style(self)
        style.theme_use("default")

        style.configure(
            "Menu.TButton",
            font=BUTTON_FONT,
            padding=10,
            background=BUTTON_COLOR
        )

        style.configure(
            "Menu.B2Menu.TButton",
            font=BACK_TO_MENU_FONT,
            padding=10,
            background=BUTTON_COLOR
        )

        style.map(
            "Menu.TButton",
            background=[("active", ACTIVE_BUTTON_COLOR)]
        )

        style.map(
            "Menu.B2Menu.TButton",
            background=[("active", ACTIVE_BUTTON_COLOR)]
        )

        # --- Button Callbacks ---
        def start_hardware():
            status_var.set("Running")
            print("Hardware START command issued")
            messagebox.showinfo("Control", "Hardware START command issued")
            # TODO: Add real hardware control logic here

        def stop_hardware():
            status_var.set("Stopped")
            print("Hardware STOP command issued")
            messagebox.showinfo("Control", "Hardware STOP command issued")
            # TODO: Add real hardware control logic here
            
        def power_hardware():
            status_var.set("Power On")
            print("Hardware Turned on")
            messagebox.showinfo("Control", "Hardware Power On")
            # TODO: Add real hardware control logic here


        
        control_title = tk.Label(self, text="Control Page", font=TITLE_FONT)
        control_title.configure(bg=BACKGROUND_COLOR, fg="white")
        control_title.pack(pady=10)

        # --- Back to Menu Button ---
        btn = ttk.Button(
            self,
            text="Back to Main Menu",
            style="Menu.B2Menu.TButton",
            command=lambda: app.show_frame("MainMenu")
        )
        btn.pack(side="bottom", anchor="e", padx=10, pady=10)
    
        # --- Status Label ---
        status_var = tk.StringVar(value="Idle")
        status_label = tk.Label(self, textvariable=status_var, font=SUBTITLE_FONT)
        
        status_label.configure(bg=BACKGROUND_COLOR, fg="white")
        status_label.pack(pady=10)  

        # --- Buttons ---
        on_button = ttk.Button(
            self, 
            text="Power On", 
            style="Menu.TButton",
            command=power_hardware)
        on_button.pack(pady=10)

        start_button = ttk.Button(
            self, 
            text="Start", 
            style="Menu.TButton",
            command=start_hardware)
        start_button.pack(pady=10)

        stop_button = ttk.Button(
            self, 
            text="Stop", 
            style="Menu.TButton", 
            command=stop_hardware)
        stop_button.pack(pady=10)