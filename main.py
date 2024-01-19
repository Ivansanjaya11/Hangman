import tkinter as tk
from pages.game_easy import game_easy
from pages.home import home_page
from pages.difficulty import difficulty_page
from pages.game_medium import game_medium
from pages.game_hard import game_hard


class Hangman_the_game:
    def __init__(self, root):
        self.root = root
        self.pages = {
            "home": home_page,
            "difficulty": difficulty_page,
            "game_easy": game_easy,
            "game_medium": game_medium,
            "game_hard": game_hard
        }
        self.current_page = None
        self.difficulty = None
        self.show_page("home")


    def show_page(self, page_name):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = self.pages[page_name](self.root, self)
        self.current_page.pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    root = tk.Tk()
    #root.attributes('-fullscreen', True)
    root.state('zoomed')
    root.title('Hangman Game')
    HangmanGame = Hangman_the_game(root)
    root.show_page = HangmanGame.show_page
    root.mainloop()