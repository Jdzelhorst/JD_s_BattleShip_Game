"""
Random was needed to create random integers
Os was imported to clear the screen after an updated board
Sys was imported to reset the system in the restart game function
"""
import random
import os
import sys


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
        difficulty = int(input("     What difficulty do you choose?(1-3): \n"))
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
            num_ships = int(16)
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


# I saw AVTpepper use this, but I didn't know why untill testing
def justifying_board_size():
    """
    This function is needed to stop the board from multiplying during the game
    """
    for x in range(board_size):
        board.append([" "] * board_size)
    return board_size


# This function is based on the code AVTpepper
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


# This function is inspired by the code AVTpepper
def build_ship():
    """
    The ships will be made here.
    The amount of ships is based on the difficulty chosen by the user.
    The idea is to make 1x1 ships on random coordinates
    A future idea is to make the ships longer
    and to be orientated horizontally or vertically
    """
    ships_build = 0
    while ships_build != num_ships:
        ship_row = random.randint(1, (board_size))
        ship_col = random.randint(1, (board_size))
        location = [ship_row, ship_col]
        ship_placement.append(location)
        ships_build += 1


# This function is inspired by the code AVTpepper
def making_guesses():
    """
    This function will take input from the user.
    Check the input against the placement of this ships.
    Record the guess and give output through the terminal.
    Changes the board according to hit or miss.
    """
    global attempts
    ships_hit = 0
    tries = (num_ships * 2.5)
    for attempts in range(int(tries)):
        print(" ")
        print(f"            You have {int(tries - attempts)} attempts left")
        print(f"            There are {len(ship_placement)} ships left ")
        guess_row = None
        while True:
            guess_row = input("             Enter a row number: \n")
            if guess_row.isdigit():
                guess_row = int(guess_row)
                break
            else:
                build_board()
                print("No can do! Try a number shown on the left of the grid")
                continue
        guess_col = None
        while True:
            guess_col = input("             Enter column letter: \n")
            if guess_col.isalpha() and len(guess_col) == 1:
                guess_col = guess_col.lower()
                guess_col = ord(guess_col) - 96
                break
            else:
                build_board()
                print(" That's not possible, try a coordinate within the grid")
                continue
        guess = [guess_row, guess_col]
        if guess in ship_placement:
            os.system('clear')
            print("*******************************************************")
            print("             You hit a ship!")
            print("_______________________________________________________")
            board[guess_row - 1][guess_col - 1] = "X"
            ship_placement.remove(guess)
            ships_hit += 1
        elif (attempts + 1) - tries == 0:
            os.system('clear')
            print("*******************************************************")
            print("             You are out of ammo!")
            print("                Game Over...")
            print("_______________________________________________________")
        elif (guess_row < 1 or guess_row > board_size):
            os.system('clear')
            print("*******************************************************")
            print("That's not possible, try a coordinate within the grid")
            print("_______________________________________________________")
        elif (guess_col < 1 or guess_col > board_size):
            os.system('clear')
            print("*******************************************************")
            print("That's not possible, try a coordinate within the grid")
            print("_______________________________________________________")
        elif (board[guess_row - 1][guess_col - 1]) == "X":
            os.system('clear')
            print("*******************************************************")
            print("         You guessed that one already...")
            print("_______________________________________________________")
        elif (board[guess_row - 1][guess_col - 1]) == "-":
            os.system('clear')
            print("*******************************************************")
            print("         You guessed that one already...")
            print("_______________________________________________________")
        else:
            os.system('clear')
            print("*******************************************************")
            print("             You missed! Try again!")
            print("_______________________________________________________")
            board[guess_row - 1][guess_col - 1] = "-"
        if ships_hit == num_ships:
            os.system('clear')
            build_board()
            print("*******************************************************")
            print("   Congratulations, you have hit all the ships!")
            print("_______________________________________________________")
            break
        build_board()
    attempts += 1


def main():
    """
    This is the main function.
    It calls all the necessary functions to play the game
    """
    choose_difficulty()
    os.system('clear')
    welcome_message()
    justifying_board_size()
    build_board()
    build_ship()
    # print(ship_placement)
    """
    Uncomment to see the ship location (used for testing)
    """
    making_guesses()


def restart_game():
    """
    This function gives the user the option to play the game again.
    """
    print(" ")
    print(" ")
    print("           The Game is over!")
    while True:
        play_again = input("     Do you want to play again? y/n: \n")
        if play_again == "y":
            # The code below was taken from Stackoverflow.
            # See the readme for more information.
            os.execv(sys.executable, [sys.executable] + sys.argv)
            break
        elif play_again == "n":
            print("Okay, your choice! See you again soon!")
            sys.exit()
            break
        else:
            print("     Invalid answer, answer with y or n")
            continue


"""
Below here are all the variables used througout the multiple functions
"""
board_size = int()
num_ships = int()
attempts = int()
board = []
ships_build = []
ship_placement = []

"""
Calling the needed functions below
"""
main()
restart_game()
