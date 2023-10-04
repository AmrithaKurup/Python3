from typing import List

game_on = True
game_board_position = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
game_board_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
count = 0
player_choice = 'Player 1'


print('The position of the board looks like this')
print(game_board_position[6]+'  | '+game_board_position[7]+' | '+game_board_position[8])
print('---|---|---')
print(game_board_position[3]+'  | '+game_board_position[4]+' | '+game_board_position[5])
print('---|---|---')
print(game_board_position[0]+'  | '+game_board_position[1]+' | '+game_board_position[2])
print('Player 1 enter X')
print('Player 2 enter O')
print('Now the game begins!!!')

def display_board(game_board):
    print(game_board[6]+'  | '+game_board[7]+' | '+game_board[8])
    print('---|---|---')
    print(game_board[3]+'  | '+game_board[4]+' | '+game_board[5])
    print('---|---|---')
    print(game_board[0]+'  | '+game_board[1]+' | '+game_board[2])

def position_choice(player_choice):
    choice = '10'

    while choice not in game_board_index:
        choice = input(f'{player_choice} : please select a position from {game_board_index} : ')

        if choice not in game_board_index:
            print('Oops! You have entered wrong')

    return int(choice)

def replecement_choice_1(game_board, position):
    game_board[position] = 'X'
    return game_board

def replecement_choice_2(game_board, position):
    game_board[position] = 'O'
    return game_board

while game_on:
    display_board(game_board)
    position = position_choice(player_choice)
    if player_choice == 'Player 1':
        replecement_choice_1(game_board, position)
        player_choice = 'Player 2'
    else:
        replecement_choice_2(game_board, position)
        player_choice = 'Player 1'
    game_board_index[position] = ''
    count = count+1

    if game_board[0] == game_board[1] == game_board[2] == 'X' or game_board[3] == game_board[4] == game_board[5] == 'X' or game_board[6] == game_board[7] == game_board[8] == 'X' or game_board[0] == game_board[3] == game_board[6] == 'X' or game_board[1] == game_board[4] == game_board[7] == 'X' or game_board[2] == game_board[5] == game_board[8] == 'X' or game_board[0] == game_board[4] == game_board[8] == 'X' or game_board[6] == game_board[4] == game_board[2] == 'X':
        print('Player 1 won!')
        display_board(game_board)
        game_on = False
    elif game_board[0] == game_board[1] == game_board[2] == 'O' or game_board[3] == game_board[4] == game_board[5] == 'O' or game_board[6] == game_board[7] == game_board[8] == 'O' or game_board[0] == game_board[3] == game_board[6] == 'O' or game_board[1] == game_board[4] == game_board[7] == 'O' or game_board[2] == game_board[5] == game_board[8] == 'O' or game_board[0] == game_board[4] == game_board[8] == 'O' or game_board[6] == game_board[4] == game_board[2] == 'O':
        print('Player 2 won!')
        display_board(game_board)

        game_on = False
    else:
        if count == 9:
            print('Its a draw!\nPlay again')
            game_on = False


