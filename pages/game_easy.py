import tkinter as tk
from tkinter import *
from tkinter import Frame
import requests

api_key = "Merriam_key"
base_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=your-api-key"

def get_word_definition(word):
    url = f'{base_url}/collegiate/json/{word}'
    params = {'key': api_key}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        definitions = response.json()
        for definition in definitions:
            print(definition)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


class home_page(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.controller = controller
        self.canvas = tk.Canvas(self, width=master.winfo_screenwidth(), height=master.winfo_screenheight(), bg="white")

        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.initial_objects()
        wrong = 0

    def initial_objects(self):
        self.canvas.create_line(250, 650, 350, 650)  # base
        self.canvas.create_line(300, 650, 300, 200)  # pole
        self.canvas.create_line(300, 200, 475, 200)  # beam
        self.canvas.create_line(475, 200, 475, 250)  # rope

    def make_a_mistake(self, master):
        if self.wrong == 0:
            return
        elif self.wrong == 1:
            self.canvas.create_oval(450, 250, 500, 300)
        elif self.wrong == 2:
            self.canvas.create_line(475, 300, 475, 425)
        elif self.wrong == 3:
            self.canvas.create_line(475, 315, 425, 420)
        elif self.wrong == 4:
            self.canvas.create_line(475, 315, 525, 420)
        elif self.wrong == 5:
            self.canvas.create_line(475, 425, 425, 525)
        elif self.wrong == 6:
            self.canvas.create_line(475, 425, 525, 525)
            blur_box = self.canvas.create_rectangle(0, 0, 2000, 1000, fill="black",stipple='gray50')
            game_over = tk.Label(master, text="GAME OVER", font=(None, 50))
            game_over.place(relx=0.5, rely=0.5, anchor=CENTER)