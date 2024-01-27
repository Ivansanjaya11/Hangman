# Hangman using Python & Tkinter
Hangman project

# Overview
This app is a simple Hangman game. Its purpose is to encourage English learners to learn new words. The goal of the project, as
a developer, is to familiarize themselves with Tkinter as a GUI module. In the future, there will be new implementations such as
an unlimited mode with leaderboards


# Key topics
1. Python
- Making a hangman algorithm for each difficulty setting
- Using classes and functions to break up the algorithm for ease off the reading process

2. Tkinter
- Creating buttons
- Creating labels
- Creating a timer
- Creating shapes
- Creating entry boxes
- Event binding
- Using Frame, master, and controller to define multiple canvases (pages) in one root (window)

3. Using API
- Using Request module to get a json file from Merriam-Webster API
- Data parsing and display

4. Miscellaneous topics
- Using wonderwords module (random word generator)
- Using pygame module (audio output)
- Using Hovertip module (showing text when hovering on an object)

# Key features
1. Can adjust difficulty setting (easy, medium, hard)
2. Easy mode provides clue in the form of definition
3. Hard mode is provided with a timer that regards not answering within the allocated time as a wrong answer

# Dependencies

Make sure you have the following dependencies installed before running the project:

- Python 3.11
- tkinter
- requests 2.31.0
- pygame 2.5.2
- wonderwords 2.2.0

# How to install and run the program
1. Clone the zip file, then extract it
2. Open your IDE and choose the cloned file
3. Open your browser and go to Merriam-Webster API developer website
4. Make an account, or sign in if you already have one (https://dictionaryapi.com/)
5. Get your API key and paste it to line 44 in game_easy.py file (self.api_key = "YOUR API KEY HERE")
6. Go back to your IDE
7. Run the program
8. Enjoy the game

