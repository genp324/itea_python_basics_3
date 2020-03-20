from random import randint

money_player1 = 0
money_player2 = 0
money_player3 = 0
money_bank    = 0

count_player = 0
more = 'y'
is_play = True

count_player  = int(input('How many player will be (may be from 1 to 3) - '))
# First round
while  is_play:
    card_player1 = 0
    card_player2 = 0
    card_player3 = 0
    card_bank = 0
    bet_player1 = 0
    bet_player2 = 0
    bet_player3 = 0
    bet_bank = 0
    next_round = 0

    if  count_player == 1:
        bet_player1 = int(input(f'Player {count_player} your bet - '))
        card_player1 = randint(2,11)
        card_bank = randint(2,11)
        print(f'Player1 your card is - {card_player1}')
        print(f'Bank your card is - {card_bank}')
    # Second and more cards

        card_player1 += randint(2, 11)
        print(f'Player1 your cards are - {card_player1}')
        if card_player1 == 21 or card_player1 == 22:
            print(f'Player 1 you win! {bet_player1}')
            money_player1 += bet_player1
            money_bank -= bet_player1
            next_round = 1
        else:
            more = input('More card y/n? ')
            while more == 'y':
                card_player1 += randint(2, 11)
                print(f'Player 1 have - {card_player1}')
                if card_player1 > 21:
                    print(f'You loose! {bet_player1} $')
                    money_player1 -= bet_player1
                    money_bank += bet_player1
                    next_round = 1
                    break
                if card_player1 == 21:
                    print(f'Player 1 you win! {bet_player1} $')
                    money_player1 += bet_player1
                    money_bank -= bet_player1
                    next_round = 1
                    break
                more = input('More card y/n? ')
        if  next_round != 1:

            card_bank += randint(2, 11)
            print(f'Bank have cards - {card_bank}')
            if card_bank == 21 or card_bank == 22:
                print(f'Bank win! {bet_player1} $')
                money_player1 -= bet_player1
                money_bank += bet_player1
            else:
                more = input('More card y/n? ')
                while more == 'y':
                    card_bank += randint(2, 11)
                    print(f'Bank have - {card_bank}')
                    if card_bank > 16 and card_bank < 21:
                        break
                    if card_bank > 21:
                        print(f'Bank have - {card_bank} and loose {bet_player1} $')
                        money_player1 += bet_player1
                        money_bank -= bet_player1
                        next_round = 1
                        break
                    elif card_bank == 21:
                        print(f'Bank win! {bet_player1} $')
                        money_player1 -= bet_player1
                        money_bank += bet_player1
                        next_round = 1
                        break
                    more = input('More card for bank y/n? ')

                if next_round != 1:
                    if card_bank > card_player1:
                        print(f'Bank win! {bet_player1} $')
                        money_player1 -= bet_player1
                        money_bank += bet_player1
                    else:
                        print(f'Player 1 you win! {bet_player1} $')
                        money_player1 += bet_player1
                        money_bank -= bet_player1

    else:
        print('More then 1 player. Will be released in next releases.')
        break
    next_round = 0
    more = input('Next round y/n? ')
    if more != 'y':
        is_play = False
print ('Bay')
print (f'See score: bank have {money_bank} $, player have {money_player1} $')
