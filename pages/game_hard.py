import tkinter as tk #for GUI
from tkinter import *
from tkinter import Frame
from pygame import mixer #for generating audio output
from wonderwords import RandomWord #to randomly generate English words for the guessing game
from tkinter import *

class game_hard(Frame):
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

        self.sec = 11
        self.time = Label(self, text=10, fg='green')
        self.time.place(x=400, y = 50)
        self.tick()

        #check button to run the button_check_command (to know if it's wrong, correct, game over, or win)
        self.check_button = tk.Button(self, text='check', command=self.button_check_command, font=(None, 12))
        self.check_button.place(x=650, y=400)

        self.word.bind("<Return>", self.button_check_command)

        self.my_word = list(RandomWord().word(word_max_length=10)) #randomly generates English words
        self.my_word_string = ''.join(self.my_word) #turns list into string
        self.labels = [] #sets labels to empty list
        self.empty_boxes() #initialize the empty_boxes function

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

    def tick(self):
        self.sec -= 1
        self.time['text'] = self.sec
        # Take advantage of the after method of the Label
        self.time.after(1000, self.tick)
        if self.sec == 0:
            self.sec = 11
            self.wrong += 1
            self.make_a_mistake(self)

    '''make_a_mistake will display a part of the hangman shape each time a mistake is made. 
    When the hangman picture is complete and the player haven't guessed the word, 
    the function will display a game over text and a mocking audio'''
    def make_a_mistake(self, master):
        if self.wrong == 0:
            return
        elif self.wrong == 1:
            self.canvas.create_oval(450, 250, 500, 300) # head
            self.sec = 11
        elif self.wrong == 2:
            self.canvas.create_line(475, 300, 475, 425) # body
            self.sec = 11
        elif self.wrong == 3:
            self.canvas.create_line(475, 315, 425, 420) # left hand
            self.sec = 11
        elif self.wrong == 4:
            self.canvas.create_line(475, 315, 525, 420) # right hand
            self.sec = 11
        elif self.wrong == 5:
            self.canvas.create_line(475, 425, 425, 525) # left leg
            self.sec = 11
        elif self.wrong == 6:
            self.canvas.create_line(475, 425, 525, 525) # right leg
            self.time.destroy()
            blur_box = self.canvas.create_rectangle(0, 0, 2000, 1000, fill="black",stipple='gray50') #blurs the whole screen
            game_over = tk.Label(master, text="GAME OVER", font=(None, 50)) # shows GAME OVER text
            game_over.place(relx=0.5, rely=0.5, anchor=CENTER) #places GAME OVER in the center of the screen
            solution = tk.Label(master, text=f'The answer is {self.my_word_string}', font=(None, 25))
            solution.place(relx=0.5, rely=0.6, anchor=CENTER)
            mixer.init() #initialize the pygame.mixer module
            mixer.music.load('audio/laughing_dog.mp3') #loads an mp3 file
            mixer.music.play() #starts the mp3 file

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
                self.sec = 11
        if count==0:
            self.wrong+=1
            self.make_a_mistake(self)
        if all(label.cget("text") != '' for label in self.labels):
            blur_box = self.canvas.create_rectangle(0, 0, 2000, 1000, fill="black",stipple='gray50') #blurs the whole screen
            self.time.destroy()
            win = tk.Label(self, text="You win", font=(None, 50))
            win.place(relx=0.5, rely=0.5, anchor=CENTER)
            mixer.init()
            mixer.music.load('audio/victory_fanfare.mp3')
            mixer.music.play()
        self.word.delete(0, "end")