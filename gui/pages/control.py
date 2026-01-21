import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

class Control(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        my_font = font.Font(family="Times New Roman", size=16)

        tk.Label(self, text="Control Page", font=("Arial", 14)).pack(pady=10)

        btn = tk.Button(
            self,
            text="Back to Main Menu",
            command=lambda: app.show_frame("MainMenu")
        )
        btn.pack(side="bottom", anchor="e", padx=10, pady=10)
        

        status_var = tk.StringVar(value="Idle")
        status_label = tk.Label(self, textvariable=status_var, font=my_font)
        status_label.pack(pady=10)

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

        # --- Buttons ---
        on_button = tk.Button(self, text="Power On", font=my_font, width=15, command=power_hardware)
        on_button.pack(pady=10)

        start_button = tk.Button(self, text="Start", font=my_font, width=15, command=start_hardware)
        start_button.pack(pady=10)

        stop_button = tk.Button(self, text="Stop", font=my_font, width=15, command=stop_hardware)
        stop_button.pack(pady=10)