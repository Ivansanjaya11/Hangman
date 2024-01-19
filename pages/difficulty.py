import tkinter as tk #for GUI
from tkinter import Frame
from idlelib.tooltip import Hovertip #for displaying text when hovering over it

class difficulty_page(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.controller = controller

        #initialize the canvas
        self.canvas = tk.Canvas(self, width=master.winfo_screenwidth(), height=master.winfo_screenheight(), bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        #initialize the create_objects function
        self.create_objects()

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
        self.back = tk.Button(self, text="←", command=self.go_back, width=10, font=(None, 35)) #presses button to call go_back function
        self.back.place(x=0, y=0)
        self.easy = tk.Button(self, text="Easy", command=self.go_to_easy, width=10, font=(None, 35)) #presses button to call go_to_easy function
        self.easy.place(x=850, y=250)
        easy_tip = Hovertip(self.easy, "Displays the word's meaning")
        self.medium = tk.Button(self, text="Medium", command=self.go_to_medium, width=10, font=(None, 35)) ##presses button to call go_to_medium function
        self.medium.place(x=850, y=350)
        medium_tip = Hovertip(self.medium, "No display")
        self.hard = tk.Button(self, text="Hard", command=self.go_to_hard, width=10, font=(None, 35)) #presses button to call go_to_hard function
        self.hard.place(x=850, y=450)
        hard_tip = Hovertip(self.hard, "No display and time limit 20 seconds per guess")

    def go_to_easy(self):
        self.master.show_page("game_easy")

    def go_to_medium(self):
        self.master.show_page("game_medium")

    def go_to_hard(self):
        self.master.show_page("game_hard")

    def go_back(self):
        self.master.show_page('home')