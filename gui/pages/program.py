import tkinter as tk

class Program(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent)

        tk.Label(self, text="Program Page", font=("Arial", 14)).pack(pady=10)

        entry = tk.Entry(self, width=25)
        entry.pack(pady=20)

        label = tk.Label(self, text="")
        label.pack(pady=10)

        button = tk.Button(self, text="Submit", command=self.get_input)
        button.pack(pady=5)

        tk.Button(self, text="Back to Main Menu",
                  command=lambda: app.show_frame("MainMenu")).pack(pady=5)
        
    
    def get_input(self):
        user_text = self.entry.get()  # Get text from the Entry widget
        print("User input:", user_text)
        self.label.config(text=f"You entered: {user_text}")