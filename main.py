# =================================================================================================
# Tic Tac Toe
# =================================================================================================


import os
from time import sleep
from random import choice


# Constants----------------------------------------------------------------------------------------

BOARD = [0, 1, 2, 3, 4, 5, 6, 7, 8]
DROP_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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

# Move---------------------------------------------------------------------------------------------
def make_move(position :int, player: str, sets: set):
    board(position, player)
    sets.add(position)    
    DROP_LIST.remove(position)


# Check for win------------------------------------------------------------------------------------
def check_for_win(a:set, b:set) -> int:
    for win in WINNING_SEQUENCE:
        if win.issubset(a): 
            return True
        if win.issubset(b):
            return False
    return None
    

    

# Board--------------------------------------------------------------------------------------------

def clear_screen():
    # Clears multi-line terminal outputs across Windows or Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def board(a:tuple, player: dict):
    # Show initial state
    clear_screen()
    print(get_table())

    sleep(.5)
    BOARD[a] = player
    clear_screen()
    print(get_table())

player_1_choice = set()
player_2_choice = set()


# Game---------------------------------------------------------------------------------------------

print(get_table())
def game():
    decision = input('Wanna move first; type "y" for YES or "n" for no:\n').lower()

    while decision not in ('y', 'n', 'end'):
        decision = input('invalid input, TRY AGAIN: ').lower()

    if decision== 'end':
        return
    else : 
        user = (decision == 'y')


    while DROP_LIST:

        if user:            
            while True:
                try:
                    position = int(input("Which position would you like to select (0-8)? "))
                    if position in DROP_LIST:
                        break
                    print("Position already taken or invalid choice.")
                except ValueError:
                    print("Please enter a valid number (0-8).")
            symbol = "X"
            reqd_set = player_1_choice                 
    
        else:
            print("Computer is thinking")
            for _ in range(3):
                sleep(0.25)
                print(".")
            position = choice(DROP_LIST)
            symbol = 'O'
            reqd_set = player_2_choice

        make_move(position, symbol, reqd_set)


        if check_for_win(player_1_choice, player_2_choice) == True:
            print("Player 1 won")
            break
        elif check_for_win(player_1_choice, player_2_choice) == False:
            print("Player 2 won")
            break
        elif len(player_2_choice) + len(player_1_choice) == len(BOARD) :
            print("IT'S A DRAW")
            

        user = not user


if __name__ == "__main__":
    game()
