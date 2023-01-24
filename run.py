# Imports
import random
import os

board_size = int(0)
row_size = board_size
col_size = board_size
board = []
ship_placement = []

print("Welcome to JD's Battleship!")
print("Select the difficulty you want to play")
print("1 is the easiest and 3 is the hardest")
while True:
    """
    Here the user can choose the difficulty of the game.
    The difficulty is equal to the size of the board.
    That's why the input variable is called board_size.
    The size of the board also has inpact on the amount of ships and
    number of tries the user has to win the game
    """
    difficulty = int(input("What difficulty do you choose?(1-10)"))
    if difficulty == 1:
        board_size = int(3)
        num_ships = int(1)
        print(f"You have chosen {difficulty} as difficulty, good luck!")
        break
    elif difficulty == 2:
        board_size = int(6)
        num_ships = int(3)
        print(f"You have chosen {difficulty} as difficulty, good luck!")
        break
    elif difficulty == 3:
        board_size = int(10)
        num_ships = int(5)
        print(f"You have chosen {difficulty} as difficulty, good luck!")
        break
    else:
        print("You need to enter a difficulty between 2 and 10")
        continue


def welcome_message():
    """
    The welcome message of the game.
    Only shows after the user adjusted the settings.
    """
    print("Welcome to JD's Battleship!")
    print("There are multiple battleships hidden in this board.")
    print("Insert the coordinates you think an enemy ship is hiding.")


def build_board():
    """
    Creates the board and prints it.
    """
    for x in range(board_size):
        board.append([" "] * board_size)

    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    column_letters = alphabet[0: (board_size)]
    print("      %s%s" % (" ", " ".join(column_letters)))
    row_number = 1
    for row in board:
        if row_number <= 9:
            print("     %d|%s|" % (row_number, "|".join(row)))
        else:
            print("    %d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# Ships


def build_ship():
    """
    The ships will be made here.
    The amount of ships is based on the difficulty chosen by the user.
    The idea is to make ships with a minimal lenght of 2, either horizontal or vertical.
    """
    ships_build = 0
    while ships_build != num_ships:
        len_ship = random.randint(1, board_size - 4)
        orientation = random.randint(0, 1)
        if orientation == 0:
            row_ship = [random.randint(0, board_size - 1)] * len_ship
            col = random.randint(0, board_size - len_ship)
            col_ship = list(range(col, col + len_ship))
            location = (row_ship, col_ship)
            ship_placement.append(location)
            ships_build +=1
        else:
            col_ship = [random.randint(0, board_size - 1)] * len_ship
            row = random.randint(0, board_size - len_ship)
            row_ship = list(range(row, row + len_ship))
            location = (row_ship, col_ship)
            ship_placement.append(location)
            ships_build +=1



def main():
    os.system('clear')
    welcome_message()
    
    
    
    build_board()




# Game Start


# Playing Board

# Game End