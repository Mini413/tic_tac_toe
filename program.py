import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Global constants
QUIT = "2"

# Interface that provides a method to create a layout in the terminal
class terminal_format():
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def gui_layout():
        pass

# A menu that the user can select options from
@dataclass
class Menu():
    title: str = "None"
    mode1: str = "None"
    quit: str = "Quit"

    def gui_layout(self):
        print(f"##### {self.title} #####\n1) {self.mode1}\n2) {self.quit}")

# Tic-tac-toe board
class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def gui_layout(self):
        print(f"+-----------+")
        print(f"| {self.cells[0]} | {self.cells[1]} | {self.cells[2]} |")
        print(f"|-----------|")
        print(f"| {self.cells[3]} | {self.cells[4]} | {self.cells[5]} |")
        print(f"|-----------|")
        print(f"| {self.cells[6]} | {self.cells[7]} | {self.cells[8]} |")
        print(f"+-----------+")

#### MAIN ####
os.system("cls")
menu = Menu("Tic-Tac-Toe", "New Game")
val = ""

# Begins game loop
while val != QUIT:
    print(menu.gui_layout())
    val = input("Please select an option: ")
    
    # Validates user input and does the correct actions according to the choice
    if val == "1":
        os.system("cls")
        winner = False
        gameBoard = Board()
        print(gameBoard.gui_layout())
        
        # while winner == False:
        #     play1 = int(input("Place your 'X' by entering 1-9: "))
        #     if play1 == range(1,10):

    elif val == QUIT:
        print("Thank you for playing!")

    else:
        print("Please enter a valid option. HINT: Select one of the numbers listed.")

