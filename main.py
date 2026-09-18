# =================================================================================================
# Tic Tac Toe
# =================================================================================================


import os
from time import sleep
from random import randint


# Constants----------------------------------------------------------------------------------------
PLAYERS = {
    'player 1' : 'X',
    'player 2' : 'O' ,
}

BOARD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

WINNING_SEQUENCE = (
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
    {0, 4, 8}, {2, 4, 6},
)

def get_table():
    return f'''

                          |            |
                          |            |
                          |            |
                   {BOARD[0]}      |     {BOARD[1]}      |     {BOARD[2]}
                          |            |
                          |            |
                          |            |
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                   {BOARD[3]}      |     {BOARD[4]}      |     {BOARD[5]}
                          |            |
                          |            |
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                   {BOARD[6]}      |     {BOARD[7]}      |     {BOARD[8]}
                          |            |
                          |            |
                          |            |

'''




# Board--------------------------------------------------------------------------------------------

def clear_screen():
    # Clears multi-line terminal outputs across Windows or Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def board():
    # Show initial state
    clear_screen()
    print(get_table())
    
    for i in range(0, 9):
        sleep(1)
        BOARD[i] = 'X'
        clear_screen()
        print(get_table())

# Move---------------------------------------------------------------------------------------------
def make_move():
    pass


# Check for win------------------------------------------------------------------------------------
def check_for_win():
    pass


if __name__ == "__main__":
    board()
