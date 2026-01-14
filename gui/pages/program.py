import tkinter as tk
from tkinter import font
from tkinter import messagebox

class Program(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent)
        my_font = font.Font(family="Times New Roman", size=16)

        tk.Label(self, text="Delay Between Messages (ms):", font=my_font).pack(pady=(10, 0))
        delay_entry = tk.Entry(self, font=my_font)
        delay_entry.pack(pady=5)

        tk.Label(self, text="Start Delay (ms):", font=my_font).pack(pady=(10, 0))
        start_delay_entry = tk.Entry(self, font=my_font)
        start_delay_entry.pack(pady=5)

        tk.Label(self, text="Iterations:", font=my_font).pack(pady=(10, 0))
        duration_entry = tk.Entry(self, font=my_font)
        duration_entry.pack(pady=5)

        btn = tk.Button(
            self,
            text="Back to Main Menu",
            command=lambda: app.show_frame("MainMenu")
        )

        btn.pack(side="bottom", anchor="e", padx=10, pady=10)

        
        def save_values():
            try:
                duration = float(duration_entry.get())
                delay = float(delay_entry.get())
                start_delay = float(start_delay_entry.get())
                print(f"Saved values: duration={duration}, delay={delay}, start_delay={start_delay}")
                messagebox.showinfo("Saved", "Settings saved successfully!")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid numbers.")

        save_button = tk.Button(self, text="Save", command=save_values, font=my_font)
        save_button.pack(pady=20)
