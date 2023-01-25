# Imports
import random
import os

board_size = int(0)
board = []
ship_placement = []


def choose_difficulty():
    """
    Here the user can choose the difficulty of the game.
    The difficulty is equal to the size of the board.
    That's why the input variable is called board_size.
    The size of the board also has inpact on the amount of ships and
    number of tries the user has to win the game
    """
    os.system('clear')
    print("           Welcome to JD's Battleship!")
    print("     Select the difficulty you want to play")
    print("    1 is easy, 2 is normal and 3 is for hard")
    global board_size
    global num_ships
    while True:
        difficulty = int(input("     What difficulty do you choose?(1-3): "))
        if difficulty == 1:
            board_size = int(3)
            num_ships = int(2)
            print(f"You have chosen {difficulty} as difficulty, good luck!")
            break
        elif difficulty == 2:
            board_size = int(6)
            num_ships = int(8)
            print(f"You have chosen {difficulty} as difficulty, good luck!")
            break
        elif difficulty == 3:
            board_size = int(10)
            num_ships = int(15)
            print(f"You have chosen {difficulty} as difficulty, good luck!")
            break
        else:
            print("You need to enter a difficulty between 1 and 3")
            continue


def welcome_message():
    """
    The welcome message of the game.
    Only shows after the user adjusted the settings.
    """
    print("           Welcome to JD's Battleship!")
    print("  There are multiple battleships hidden in this board.")
    print(" Insert the coordinates you think an enemy ship is hiding.")


def justifying_board_size():
    """
    This function is needed to stop the board from multiplying during the game
    """
    for x in range(board_size):
        board.append([" "] * board_size)
    return board_size


def build_board():
    """
    Creates the board and prints it.
    """
    global alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    column_letters = alphabet[0: (board_size)]
    print("                 %s%s" % (" ", " ".join(column_letters)))
    row_number = 1
    for row in board:
        if row_number <= 9:
            print("                %d|%s|" % (row_number, "|".join(row)))
        else:
            print("               %d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def build_ship():
    """
    The ships will be made here.
    The amount of ships is based on the difficulty chosen by the user.
    The idea is to make ships with a minimal lenght of 2,
    either horizontal or vertical.
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
            ships_build += 1
        else:
            col_ship = [random.randint(0, board_size - 1)] * len_ship
            row = random.randint(0, board_size - len_ship)
            row_ship = list(range(row, row + len_ship))
            location = (row_ship, col_ship)
            ship_placement.append(location)
            ships_build += 1


def user_guess():
    """
    This function is for the guesses to be made by the user.
    The idea is for the user to put coordinates in the terminal,
    to shoot at the created ships.
    """


def main():
    os.system('clear')
    welcome_message()
    build_board()
    build_ship()


main()
