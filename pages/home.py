import tkinter as tk
from tkinter import Frame

class home_page(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.controller = controller

        #initialize canvas
        self.canvas = tk.Canvas(self, width=master.winfo_screenwidth(), height=master.winfo_screenheight(), bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.create_objects() #initialize create_objects function

    def create_objects(self):
        self.canvas.create_line(250, 650, 350, 650)  # base
        self.canvas.create_line(300, 650, 300, 200)  # pole
        self.canvas.create_line(300, 200, 475, 200)  # beam
        self.canvas.create_line(475, 200, 475, 250)  # rope
        self.canvas.create_oval(450, 250, 500, 300)  # head
        self.canvas.create_line(475, 300, 475, 425)  # body
        self.canvas.create_line(475, 315, 425, 420)  # left hand
        self.canvas.create_line(475, 315, 525, 420)  # right hand
        self.canvas.create_line(475, 425, 425, 525)  # left leg
        self.canvas.create_line(475, 425, 525, 525)  # right leg

        #presses start to initialize go_to_difficulty_page function, which shows the choosing difficulty page
        self.start_button = tk.Button(self, text="Start", command=self.go_to_difficulty_page, width= 10,font=(None, 35))
        self.start_button.place(x=850, y = 350)

    def go_to_difficulty_page(self):
        self.master.show_page("difficulty")