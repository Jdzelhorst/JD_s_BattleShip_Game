# Imports
from random import randint
import os

#Standard settings
row_size = 8 
col_size = 8 
num_ships = 5
num_turns = 20 

def change_settings():
    #The user can change the settings here
    while True:
        row_size = int(input("How many rows do you prefer? (1-10) "))
        return row_size
        continue
        col_size = int(input("How many columns do you prefer? (1-10) "))
        return col_size
        num_ships = int(input("How many ships do you prefer? (1-10) "))
        return num_ships
        num_turns = int(input("In how many turns will you destroy these ships? (1-10) "))
        return num_turns

#Playing Board
game_board = [["O"] * col_size for _ in range(row_size)]
for board in game_board:
    print(*board)
#Ships

#Welcome message
def welcome_message():
    print("Welcome to JD's Battleship!")
    print("There are multiple battleships hidden in this board. Enter your row and column guesses to sink it!')

#Game Start

#Game End