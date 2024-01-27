import tkinter as tk #for GUI
from tkinter import *
from tkinter import Frame
import requests #for requesting API Merriem Webster (used to display word meaning)
from pygame import mixer #for generating audio output
from wonderwords import RandomWord #to randomly generate English words for the guessing game

class game_easy(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.controller = controller

        #displays the canvas
        self.canvas = tk.Canvas(self, width=master.winfo_screenwidth(), height=master.winfo_screenheight(), bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        #displays go back button to allow players to exit the game back to the choosing difficulty page
        self.back = tk.Button(self, text="←", command=self.go_back, width=10, font=(None, 35))
        self.back.place(x=0, y=0)

        self.initial_objects() #initialize the initial_objects function
        self.wrong = 0 #sets the wrong variable to 0 (to be used in button_command_function)

        #input the guessed alphabet of the word
        self.word = tk.Entry(self, borderwidth=5, width=10, font=(None, 12))
        self.word.place(x=650, y=350)

        #check button to run the button_check_command (to know if it's wrong, correct, game over, or win)
        self.check_button = tk.Button(self, text='check', command=self.button_check_command, font=(None, 12))
        self.check_button.place(x=650, y=400)

        self.word.bind("<Return>", self.button_check_command)

        self.my_word = list(RandomWord().word(word_max_length=10)) #randomly generates English words
        self.my_word_string = ''.join(self.my_word) #turns list into string
        self.labels = [] #sets labels to empty list
        self.empty_boxes() #initialize the empty_boxes function

        #sets the label for the clue in the easy difficulty (word meaning)
        self.meaning_label = Label(self, text='', wraplength=525, width=75, borderwidth=0, font=(None, 12),justify=LEFT)
        self.meaning_label.place(x=650, y=225)

        #sets the api
        self.api_key = "Your_API_Key"
        self.base_url = "https://dictionaryapi.com/api/v3/references/collegiate/json"
        self.url = f'{self.base_url}/{self.my_word_string}'
        self.params = {'key': self.api_key}
        self.response = requests.get(self.url, params=self.params)
        self.data = self.response.json()

        self.get_word_details() #initialize the get_word_details that uses the API

    '''empty_boxes displays the initial blank boxes and lines. 
    The for loop defines the blank boxes and lines' length based on the length of the randomly generated word'''
    def empty_boxes(self):
        for num in range(len(self.my_word)):
            label = Label(self.canvas, text='', width=5, borderwidth=5, height=2, font=(None, 15), relief='solid')
            label.place(x=650+(num*70), y = 550)
            self.labels.append(label)
            self.canvas.create_line(650+(num*70), 615, 650+((num+1)*70-4), 615)

    #initial_objects displays the initial figure of the hangman object
    def initial_objects(self):
        self.canvas.create_line(250, 650, 350, 650)  # base
        self.canvas.create_line(300, 650, 300, 200)  # pole
        self.canvas.create_line(300, 200, 475, 200)  # beam
        self.canvas.create_line(475, 200, 475, 250)  # rope

    #go_back is used when the player presses the 'go back' button
    def go_back(self):
        self.master.show_page('difficulty')
        mixer.music.stop()

    '''make_a_mistake will display a part of the hangman shape each time a mistake is made. 
    When the hangman picture is complete and the player haven't guessed the word, 
    the function will display a game over text and a mocking audio'''
    def make_a_mistake(self, master):
        if self.wrong == 0:
            return
        elif self.wrong == 1:
            self.canvas.create_oval(450, 250, 500, 300) # head
        elif self.wrong == 2:
            self.canvas.create_line(475, 300, 475, 425) # body
        elif self.wrong == 3:
            self.canvas.create_line(475, 315, 425, 420) # left hand
        elif self.wrong == 4:
            self.canvas.create_line(475, 315, 525, 420) # right hand
        elif self.wrong == 5:
            self.canvas.create_line(475, 425, 425, 525) # left leg
        elif self.wrong == 6:
            self.canvas.create_line(475, 425, 525, 525) # right leg
            blur_box = self.canvas.create_rectangle(0, 0, 2000, 1000, fill="black",stipple='gray50') #blurs the whole screen
            game_over = tk.Label(master, text="GAME OVER", font=(None, 50)) # shows GAME OVER text
            game_over.place(relx=0.5, rely=0.5, anchor=CENTER) #places GAME OVER in the center of the screen
            solution = tk.Label(master, text=f'The answer is {self.my_word_string}', font=(None, 25))
            solution.place(relx=0.5, rely=0.6, anchor=CENTER)
            mixer.init() #initialize the pygame.mixer module
            mixer.music.load('audio/laughing_dog.mp3') #loads an mp3 file
            mixer.music.play() #starts the mp3 file

    '''get_word_details parses the data from the json file in the API and 
    specifically takes the meaning of a word to display'''
    def get_word_details(self):
        if isinstance(self.data, list): #checks if the data inputted is a list
            if self.data: #check if the data is not None
                first_item = self.data[0] #access the 0th index of the data

                word_meta = first_item.get("meta", {}) #pulls the meta or the word
                word_fl = first_item.get("fl", "") #pulls the part of speech
                word_def = first_item.get("shortdef", []) # pulls the definition

                #make a dictionary containing the 3 parsed content
                self.current_word = {
                    'word': word_meta.get('id', '')[:-2],
                    'part of speech': {word_fl},
                    'meaning': '; '.join(word_def)
                }

                word_details = self.current_word['meaning'] #store the value of meaning in a variable word_details
                self.meaning_label.config(text=word_details) #updates the self.meaning_label empty label into the stored meaning

    '''button_check_command is a callback funtion when player presses 'check'.
    it compares the inputted letter with the randomly generated words to see if there's a match.
    If there's a match, the empty boxes labels are updated to show the character in the appropriately indexed label.
    If there's no match in all labels, the letter is wrong (variable wrong is added by 1) and calls the make_a_mistake function.
    if all labels in the empty boxes are no longer empty, then prints a label 'You Win' in the center of the screen.
    pygame.mixer module helps to output the victory fanfare mp3 audio
    '''
    def button_check_command(self, event=None):
        entered_word = self.word.get()
        count = 0
        for idx, char in enumerate(self.my_word):
            if char == entered_word:
                self.labels[idx].config(text=char)
                count+=1
        if count==0:
            self.wrong+=1
            self.make_a_mistake(self)
        if all(label.cget("text") != '' for label in self.labels):
            blur_box = self.canvas.create_rectangle(0, 0, 2000, 1000, fill="black",stipple='gray50') #blurs the whole screen
            win = tk.Label(self, text="You win", font=(None, 50))
            win.place(relx=0.5, rely=0.5, anchor=CENTER)
            mixer.init()
            mixer.music.load('audio/victory_fanfare.mp3')
            mixer.music.play()
        self.word.delete(0, "end")