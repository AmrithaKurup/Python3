game_on = True
game_list = [1, 2, 3]


def display_list(game_list):
    print('Here is the display list')
    print(game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input('Pick a position between (0, 1, 2):')

        if choice not in ['0', '1', '2']:
            print('Sorry, You entered wrong')
    return int(choice)

def replecement_choice(game_list, position):
    user_replacement = input('type a string to replace the position')
    game_list[position] = user_replacement
    return game_list

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input('Do you want to continue (Y or N):')

        if choice not in ['Y', 'N']:
            print('Sorry, You entered wrong')
    if choice == 'Y':
        return True
    else:
        return False

while game_on:
    display_list(game_list)
    position = position_choice()
    game_list = replecement_choice(game_list, position)
    display_list(game_list)
    game_on = gameon_choice()