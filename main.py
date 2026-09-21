# =================================================================================================
# Tic Tac Toe
# =================================================================================================

import os
from time import sleep
from random import choice

# Constants----------------------------------------------------------------------------------------

WINNING_SEQUENCE = (
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
    {0, 4, 8}, {2, 4, 6},
)

def get_table(board):
    return f'''

                          |            |
                          |            |
                          |            |
                   {board[0]}      |     {board[1]}      |     {board[2]}
                          |            |
                          |            |
                          |            |
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                   {board[3]}      |     {board[4]}      |     {board[5]}
                          |            |
                          |            |
                          |            |
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                   {board[6]}      |     {board[7]}      |     {board[8]}
                          |            |
                          |            |
                          |            |

'''

# Computer levelwise move--------------------------------------------------------------------------
def find_move(comp_set: set, drop_list: list) -> int | None:
    """Checks if placing a move anywhere in drop_list completes a winning set."""
    for spot in drop_list:
        temp_set = comp_set | {spot}
        for win in WINNING_SEQUENCE:
            if win.issubset(temp_set):
                return spot
    return None


def minimax(ai_set: set, human_set: set, drop_list: list, is_maximizing: bool) -> int:
    """Minimax recursion for Hard Level."""
    for win in WINNING_SEQUENCE:
        if win.issubset(ai_set):
            return 10
        if win.issubset(human_set):
            return -10
    if not drop_list:
        return 0

    if is_maximizing:
        best_score = -1000
        for spot in list(drop_list):
            drop_list.remove(spot)
            ai_set.add(spot)
            score = minimax(ai_set, human_set, drop_list, is_maximizing=False)
            ai_set.remove(spot)
            drop_list.append(spot)
            best_score = max(best_score, score)

        return best_score

    else: 
        best_score = 1000
        for spot in list(drop_list):
            drop_list.remove(spot)
            human_set.add(spot)
            score = minimax(ai_set, human_set, drop_list, is_maximizing=True)
            human_set.remove(spot)
            drop_list.append(spot)
            best_score = min(best_score, score)

        return best_score


def smart_comp_move(level: str, drop_list: list, human_set: set, ai_set: set) -> int:
    """Selects computer move based on the difficulty level."""
    
    # LEVEL 1: EASY (Pure Random)
    if level == 'easy':
        return choice(drop_list)

    # LEVEL 2: MEDIUM (Win -> Block -> Center -> Random)
    elif level == 'medium':
        # 1. Check if AI can win
        win_move = find_move(ai_set, drop_list)
        if win_move is not None:
            return win_move

        # 2. Check if AI needs to block human win
        block_move = find_move(human_set, drop_list)
        if block_move is not None:
            return block_move

        # 3. Take center if open
        if 4 in drop_list:
            return 4

        # 4. Fallback to random choice
        return choice(drop_list)

    # LEVEL 3: HARD (Unbeatable Minimax Algorithm)
    elif level == 'hard':
        best_score = -1000
        best_move = drop_list[0]

        for spot in list(drop_list):
            drop_list.remove(spot)
            ai_set.add(spot)
            score = minimax(ai_set, human_set, drop_list, False)
            ai_set.remove(spot)
            drop_list.append(spot)

            if score > best_score:
                best_score = score
                best_move = spot

        return best_move


# Move---------------------------------------------------------------------------------------------
def make_move(position: int, player: str, sets: set, board_state: list, drop_list: list):
    board(position, player, board_state)
    sets.add(position)    
    drop_list.remove(position)


def user_move(drop_list: list) -> int:
    while True:
        try:
            position = int(input("Which position would you like to select (0-8)? "))
            if position in drop_list:
                return position
            print("Position already taken or invalid choice.")
        except ValueError:
            print("Please enter a valid number (0-8).")


# Check for win------------------------------------------------------------------------------------
def check_for_win(a: set, b: set) -> bool | None:
    for win in WINNING_SEQUENCE:
        if win.issubset(a):             
            return True
        if win.issubset(b):
            return False
    return None


# Board--------------------------------------------------------------------------------------------
def clear_screen():
    '''Clears multi-line terminal outputs across Windows or Mac/Linux'''
    os.system('cls' if os.name == 'nt' else 'clear')


def board(a: int, player: str, board_state: list):
    '''Show state updates'''
    clear_screen()
    print(get_table(board_state))

    sleep(.5)
    board_state[a] = player
    clear_screen()
    print(get_table(board_state))


# Game---------------------------------------------------------------------------------------------
def game():
    board_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    drop_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_1_choice = set()
    player_2_choice = set()

    clear_screen()
    print(get_table(board_state))

    players = input('Play with Computer (y/n): ').strip().lower()
    while players not in ('y', 'n'):
        players = input('invalid input, TRY AGAIN: ').strip().lower()

    with_comp = (players == 'y')

    if with_comp:
        level = input('Choose Level (1: Easy, 2: Medium, 3: Hard): ').strip()
        while level not in ('1', '2', '3'):
            level = input('Invalid level! Choose (1, 2, or 3): ').strip()

        level_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
        difficulty = level_map[level]

        decision = input('Wanna move first; type "y" for YES or "n" for no:\n').strip().lower()
        while decision not in ('y', 'n', 'end'):
            decision = input('invalid input, TRY AGAIN: ').strip().lower()

        if decision == 'end':
            return
        user = (decision == 'y')

    else:
        user = True

    while drop_list:

        if user:            
            position = user_move(drop_list)
            symbol = "X"
            reqd_set = player_1_choice                 
    
        else:
            if with_comp:
                print(f"Computer ({difficulty.upper()}) is thinking...")
                sleep(0.4)
                position = smart_comp_move(difficulty, drop_list, player_1_choice, player_2_choice)
            else: 
                position = user_move(drop_list)

            symbol = 'O'
            reqd_set = player_2_choice

        make_move(position, symbol, reqd_set, board_state, drop_list)

        result = check_for_win(player_1_choice, player_2_choice)
        if result is True:
            print("Player 1 won")
            break
        elif result is False:
            print("Computer won" if with_comp else "Player 2 won")
            break
        elif len(player_2_choice) + len(player_1_choice) == len(board_state):
            print("IT'S A DRAW")
            break

        user = not user


if __name__ == "__main__":
    game()