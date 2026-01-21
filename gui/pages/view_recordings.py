import tkinter as tk
from tkinter import font

from gui.pages.helper.load_files import load_files

class ViewRecordings(tk.Frame):
    
    def __init__(self, parent, app):
        super().__init__(parent)

        my_font = font.Font(family="Times New Roman", size=16)

        tk.Label(self, text="View Recordings Page", font=my_font).pack(pady=10)

        tk.Label(
            self, text="Select Messages (order shown on right):", font=my_font
        ).pack(pady=10)

        # Main Frame with two listboxes
        main_frame = tk.Frame(self)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)

        get_frame = tk.Frame(main_frame)
        get_frame.pack(side=tk.LEFT, padx=10, fill='both', expand=True)

        tk.Label(get_frame, text="Available Messages", font=my_font).pack()

        scroll = tk.Scrollbar(get_frame, orient=tk.VERTICAL)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        left_list = tk.Listbox(
            get_frame, font=my_font, yscrollcommand=scroll.set,
            height=12, selectmode=tk.SINGLE
        )
        files = load_files()
        for m in files:
            message = f"{m['modified']} | duration: {int(m['duration'])} | {m['filename']}"
            left_list.insert(tk.END, message)

        left_list.pack(side=tk.LEFT, fill='both', expand=True)
        scroll.config(command=left_list.yview)

        tk.Button(self, text="Back to Main Menu",
                  command=lambda: app.show_frame("MainMenu")).pack(pady=5)