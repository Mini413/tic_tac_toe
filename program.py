import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Global constants
QUIT = "2"
POS_3X3_GAME = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
CROSS = "X"
NAUGHT = "O"

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
        print(f"##### {self.title} #####\n1) {self.mode1}\n{QUIT}) {self.quit}")

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

    def place_token(self, pos, token):
        if self.cells[pos] == " ":
            self.cells[pos] = token

    def validate_token(self, pos, token1, token2):
        if self.cells[pos] == token1 or self.cells[pos] == token2 or self.cells[pos] == " ":
            return True
        else:
            print("The chosen position is occupied, please choose a different position.")
            return False

    # In future versions could turn this into a class and use composition
    def win_condition(self, token):
        if self.cells[0] == token and self.cells[1] == token and self.cells[2] == token:    #Row win conditions
            return True
        if self.cells[3] == token and self.cells[4] == token and self.cells[5] == token:
            return True
        if self.cells[6] == token and self.cells[7] == token and self.cells[8] == token:
            return True
        if self.cells[0] == token and self.cells[3] == token and self.cells[6] == token:    # Column win conditions
            return True
        if self.cells[1] == token and self.cells[4] == token and self.cells[7] == token:
            return True
        if self.cells[2] == token and self.cells[5] == token and self.cells[8] == token:
            return True
        if self.cells[0] == token and self.cells[4] == token and self.cells[8] == token:    # Diagonal win conditions
            return True
        if self.cells[2] == token and self.cells[4] == token and self.cells[6] == token:
            return True

#### MAIN ####
# Initialisation of terminal, menu and loop
os.system("cls")
menu = Menu("Tic-Tac-Toe", "New Game")
val = ""

# Begins the game by giving the user some options, similar to a case statement
while val != QUIT:
    # Initialises the menu to the screen and asks for a user choice
    print(menu.gui_layout())
    val = input("Please select an option: ")
    
    # Validates user input and does the correct actions according to the choice
    if val == "1":
        # Initialisation of variables and terminal
        os.system("cls")
        winner = False

        gameBoard = Board()
        print(gameBoard.gui_layout())
        
        # Begins the game loop
        while winner == False:
            validation = False
            ###Player 1
            while validation == False:
                # Asks for user input so the token can be placed in the correct location.
                play1 = input("Player 1, place your 'X' by entering 1-9: ")
                # Validates user input to be between the range of 1 and 9.
                while play1 not in POS_3X3_GAME:
                    print("Please enter a number between 1 and 9.")
                    play1 = input("Player 1, place your 'X' by entering 1-9: ")
                play1 = int(play1)
                validation = gameBoard.validate_token(play1, CROSS, NAUGHT)

            # Ensures that the position chosen corresponds to the correct list item
            play1 = int(play1) - 1
            # Clears old game board and places the token in the position outlined by the player
            if play1 in range(0, 9):
                os.system("cls")
                gameBoard.place_token(play1, CROSS)
                print(gameBoard.gui_layout())           
                
            # Check win condition of player 1 and finish the game
            if gameBoard.win_condition(CROSS):
                print("Player 1 (X) Wins!")
                winner = True 
                break
            
            validation = False
            ###Player 2
            while validation == False:
                # Asks for user input so the token can be placed in the correct location.
                play2 = input("Player 2, place your 'O' by entering 1-9: ")
                # Validates user input to be between the range of 1 and 9.
                while play2 not in POS_3X3_GAME:
                    print("Please enter a number between 1 and 9.")
                    play2 = input("Player 2, place your 'O' by entering 1-9: ")
                play2 = int(play2)
                validation = gameBoard.validate_token(play2, CROSS, NAUGHT)         

            # Ensures that the position chosen corresponds to the correct list item
            play2 = int(play2) - 1
            # Clears old game board and places the token in the position outlined by the player
            if play2 in range(0, 9):
                os.system("cls")
                gameBoard.place_token(play2, NAUGHT)
                print(gameBoard.gui_layout())
            
            # Check win condition of player 2
            if gameBoard.win_condition(NAUGHT):
                print("Player 2 (O) wins!")
                winner == True
    #Ends the program
    elif val == QUIT:
        print("Thank you for playing!")
    # Asks the user to select a valid option
    else:
        print("Please enter a valid option. HINT: Select one of the numbers listed.")