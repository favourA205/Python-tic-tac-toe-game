


import re
# ......global variables.......

#  Game board
board =['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']


# Current player
current_player = 'X'

# who won or tie
winner = None

# Game still going
game_still_going = True


# Display the board

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# play game function
def play_game():

# Display board function called
    display_board()

# If game is not over ,flip players to continue playing game

    while game_still_going:
        handle_turn(current_player)
# check if game is over function

        check_if_game_over()

# function to flip players
        flip_player()

# The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' wins.')
    elif winner == None:
        print('Tie')

# handle turn function
def handle_turn(player):
# Select position on the board from one to nine
    print(player + "'s turn")
    position = input('Choose position from 1-9 : ')
    valid = False
    while not valid:

        text = '1,2,3,4,5,6,7,8,9'
        pattern = re.compile('[1-9]+')
        result = pattern.findall(text)
        while position not in result:
            position = input('Choose position from 1-9 : ')

# change to integer in programming form and to computer language
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print("You can't go there. Go again!")
            position = input('Choose position from 1-9 : ')

# show player's turn

    board[position] = player


# Display the board 2
    display_board()

# Check if the game is over
def check_if_game_over():
# Check for win
    check_for_win()
# Check if there is a tie
    check_if_tie()

# Checking for win
def check_for_win():
    # Using global winner variable
    global winner
    # check rows
    row_winner = check_row()

    # check columns
    column_winner = check_column()

    # check diagonals
    diagonal_winner = check_diagonal()

# Checking for ultimate winner or if there is no winner at all
    if row_winner:
        winner =row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# Check rows
def check_row():
    global winner
    global game_still_going
    # There is a winner when all items in the row are the same except when the item is '-'
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # if the items in the row are same, the game would be over
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return winner
    if row_1:
        return board[1]
    elif row_2:
        return board[4]
    elif row_3:
        return board[7]
    return


# Check columns
def check_column():
    global winner
    global game_still_going
    # There is a winner when all items in the column are the same except when the item is '-'
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    # if the items in the column are same, the game would be over
    if column_1 or column_2 or column_3:
        game_still_going = False

    # return winner
    if column_1:
        return board[3]
    elif column_2:
        return board[4]
    elif column_3:
        return board[5]
    return

def check_diagonal():
    global winner
    global game_still_going

    # There is a winner when all items in the diagonal are the same except when the item is '-'
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    # if the items in the diagonal are same, the game would be over
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return winner
    if diagonal_1:
        return board[4]
    elif diagonal_2:
        return board[4]

    return
# Check for tie
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


# flip player
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player =='O':
        current_player = 'X'

    return

# play game
play_game()




# STEPS
 # Game board
 # Display board
 # Handle turn
  # Players
 # Game still going
 # Game over
 # win(rows,columns,diagonals)
 # Tie
 # flip players
 # Invalid input
 # Overwritting
 # scoreboard






