# Imports
import random

board_size = int(0)
row_size = board_size
col_size = board_size

print("Welcome to JD's Battleship!")
print("Select the difficulty you want to play")
print("2 is the easiest and 10 is the hardest")
while True:
    """
    Here the user can choose the difficulty of the game.
    The difficulty is equal to the size of the board.
    That's why the variable is called board_size.
    """
    board_size = int(input("What difficulty do you choose?(2-10)"))
    if board_size >1 and board_size <=10:
        print(f"Great, you have chosen {board_size} as difficulty")
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
    print("Enter your row and column guesses to sink it!")
    # build_ship(num_ships)

    
    if board_size in range(1, 11):
        return board_size

    num_ships = int(input("How many ships do you prefer? (1-10) "))
    if num_ships in range(1, 11):
        return num_ships
    else:
        print("Your answer needs to be between 1 and 10 ships!")

    num_turns = int(input("In how many turns do you prefer?"))
    if num_turns in range(10, 21):
        return num_turns
    else:
        print("Your answer needs to be 10 and 20 turns!")



def build_board():
    # The user can change the settings here
    game_board = [["O"] * col_size for _ in range(row_size)]

    for board in game_board:
        print(*board)
# Standard settings




# Ships


def build_ship(num_ships):
    # Length of ship is random number between 2 and length of board
    len_ship = random.randint(2, board_size)
    orientation = random.randint(0, 1)
    # Ship is horizontal if orientation is 0 and vertical if orientation is 1
    if orientation == 0:
        # Randomly select row and create list of selected row * length of ship
        row_ship = [random.randint(0, board_size - 1)] * len_ship
        # Randomly select column of first position of ship
        col = random.randint(0, board_size - len_ship)
        # Create list of column values
        col_ship = list(range(col, col + len_ship))
        # Create positional values from row and column lists
        coords = tuple(zip(row_ship, col_ship))
    else:
        # Same as above except switch column and row
        col_ship = [random.randint(0, board_size - 1)] * len_ship
        row = random.randint(0, board_size - len_ship)
        row_ship = list(range(row, row + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)



def main():
    welcome_message()
    
    
    
    build_board()




# Game Start


# Playing Board

# Game End