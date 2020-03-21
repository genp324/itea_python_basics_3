from random import randint

MAX_CARD = 21
PLAYER_1_CARDS = 0
PLAYER_2_CARDS = 0
PLAYER_3_CARDS = 0
PLAYER_TURN = 1
CHANCE = randint(1,2)

print('Welcome to the game, please take a card')
print(f'\nPlayer 1 your turn')

while PLAYER_TURN == 1:
    pick = randint(2,11)
    input(f'Your card is: {pick}')
    PLAYER_1_CARDS += pick
    print(f'You have {PLAYER_1_CARDS} points')

    step = input(f'\nDou you want to continue? yes/no  ')
    
    if step == 'yes':
        continue

    else:
        print(f'Player 1 has: {PLAYER_1_CARDS}')
        if PLAYER_1_CARDS > MAX_CARD:
            print('Sorry, but you lose....')
            PLAYER_1_CARDS = 0
        break

PLAYER_TURN += 1


print(f'\nPlayer 2 your turn')

while PLAYER_TURN == 2:
    pick = randint(2, 11)
    input(f'\nPlayer 2 take: {pick}')
    PLAYER_2_CARDS += pick
    print(f'Player 2 has {PLAYER_2_CARDS} points')

    if PLAYER_2_CARDS > MAX_CARD:
        print('Sorry, but you lose...')
        PLAYER_2_CARDS = 0
        break

    elif PLAYER_2_CARDS <= 13:
        continue

    else:
        if CHANCE == 1:
            print('\nI get one card')
            continue
        else:
            print(f'Player 2 has: {PLAYER_2_CARDS}')
            break

PLAYER_TURN += 1
        
print(f'\nPlayer 3 your turn')

while PLAYER_TURN == 3:
    pick = randint(2, 11)
    input(f'\nPlayer 3 take: {pick}')
    PLAYER_3_CARDS += pick
    print(f'Player 3 has {PLAYER_3_CARDS} points')

    if PLAYER_3_CARDS > MAX_CARD:
        print('Sorry, but you lose...')
        PLAYER_3_CARDS = 0
        break

    elif PLAYER_3_CARDS <= 15:
        continue

    else:
        if CHANCE == 2:
            print('\nI get one card')
            continue
        else:
            print(f'Player 3 has: {PLAYER_3_CARDS}')
            break

      

print('\nGame is closed')

if PLAYER_1_CARDS > PLAYER_2_CARDS and PLAYER_1_CARDS > PLAYER_3_CARDS:
    print(f'\nWe have the winner: Player 1')

elif PLAYER_2_CARDS > PLAYER_1_CARDS and PLAYER_2_CARDS > PLAYER_3_CARDS:
    print(f'\nWe have the winner: Player 2')

elif PLAYER_3_CARDS > PLAYER_1_CARDS and PLAYER_3_CARDS > PLAYER_2_CARDS:
    print(f'\nWe have the winner: Player 3')

else:
    print('\nWe have no winner')


    
    
    
