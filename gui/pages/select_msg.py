import tkinter as tk
from tkinter import font, messagebox

from gui.pages.helper.load_files import load_files

class SelectMsg(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent)

        my_font = font.Font(family="Times New Roman", size=16)

        tk.Label(self, text="Select Message Page", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Back to Main Menu",
                  command=lambda: app.show_frame("MainMenu")).pack(pady=5)
        
        tk.Label(
            self, text="Select Messages (order shown on right):", font=my_font
        ).pack(pady=10)

        # Main Frame with two listboxes
        main_frame = tk.Frame(self)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)

        # ---- LEFT: Available messages ----
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, padx=10, fill='both', expand=True)

        tk.Label(left_frame, text="Available Messages", font=my_font).pack()

        left_scroll = tk.Scrollbar(left_frame, orient=tk.VERTICAL)
        left_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        left_list = tk.Listbox(
            left_frame, font=my_font, yscrollcommand=left_scroll.set,
            height=12, selectmode=tk.SINGLE
        )
        files = load_files()
        for m in files:
            message = f"{m['modified']} | duration: {int(m['duration'])} | {m['filename']}"
            left_list.insert(tk.END, message)

        left_list.pack(side=tk.LEFT, fill='both', expand=True)
        left_scroll.config(command=left_list.yview)

        # ---- RIGHT: Selected order ----
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, padx=10, fill='both', expand=True)

        tk.Label(right_frame, text="Selected Order", font=my_font).pack()

        right_scroll = tk.Scrollbar(right_frame, orient=tk.VERTICAL)
        right_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        right_list = tk.Listbox(
            right_frame, font=my_font, yscrollcommand=right_scroll.set,
            height=12
        )
        right_list.pack(side=tk.LEFT, fill='both', expand=True)
        right_scroll.config(command=right_list.yview)

        # Internal list to track selected order
        selected_order = []

        # When clicking a message on left list, add to right list
        def on_left_click(event):
            index = left_list.curselection()
            if not index:
                return
            msg = left_list.get(index[0])

            # Prevent duplicates (remove this to allow repeats)
            if msg in selected_order:
                return

            selected_order.append(msg)
            right_list.insert(tk.END, msg)

        left_list.bind("<<ListboxSelect>>", on_left_click)

        # Load messages
        def load_messages():
            if not selected_order:
                self.showwarning("Warning", "Please select at least one message.")
                return

            print("Loading messages in order:")
            for msg in selected_order:
                print(msg)
            messagebox.showinfo("Load Messages", "Messages loaded successfully.")
            # TODO
            # Add microcontroller communication here

        load_button = tk.Button(
            self, text="Create", command=load_messages, font=my_font
        )
        load_button.pack(pady=10)

