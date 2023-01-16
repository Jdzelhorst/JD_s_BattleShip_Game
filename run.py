# Imports
from random import randint
import os

#Standard settings
board_size = 8
row_size, col_size = 8
num_ships = 5
num_turns = 20 

def change_settings():
    #The user can change the settings here
    row_size = int(input("How many rows do you prefer? (1-10) "))
    return row_size
    col_size = int(input("How many columns do you prefer? (1-10) "))
    return col_size
    num_ships = int(input("How many ships do you prefer? (1-10) "))
    return num_ships
    num_turns = int(input("In how many turns will you destroy these ships? (1-10) "))
    return num_turns

#Playing Board
game_board(board_size) = [["O"] * col_size for _ in range(row_size)]
for board in game_board:
    print(*board)

#Ships

def build_ship(board_size):
    # Length of ship is random number between 2 and length of board
    len_ship = random.randint(2, board_size)
    orientation = random.randint(0, 1)
    # Ship is horizontal if orientation is 0 and vertical if orientation is 1
    if orientation == 0:
        # Randomly select row and create list of selected row * length of ship
        row_ship = [random.randint(0, board_size - 1)] * len_ship
        # Randomly select column of first position of ship (Hence subtracting length of ship)
        col = random.randint(0, board_size - len_ship)
        # Create list of column values
        col_ship = list(range(col, col + len_ship))
        # Create positional values from row and column lists
        coords = tuple(zip(row_ship, col_ship))
    else:
        # Same as above except switch column and row
        col_ship = [random.randint(0, dims - 1)] * len_ship
        row = random.randint(0, board_size - len_ship)
        row_ship = list(range(row, row + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)

#Welcome message
def welcome_message():
    print("Welcome to JD's Battleship!")
    print("There are multiple battleships hidden in this board. Enter your row and column guesses to sink it!")

#Game Start

#Game End