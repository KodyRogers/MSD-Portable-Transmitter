import tkinter as tk
#from  backend.clock import Clock
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Multi-Page GUI")
        self.geometry("800x600")

        self.running = False
        #self.clock = Clock(self)
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

    def register(self, page_class):
        frame = page_class(self.container, self)
        self.frames[page_class.__name__] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        self.frames[name].tkraise()

    def toggle(self):
        self.running = not self.running



