from random import randint

BLACK_JACK = 21

game_in_progress = True

player_turn = True

dealer_turn = True

bot_1_turn = True

bot_2_turn = True

player_skipped = False

bot_1_skipped = False

bot_2_skipped = False

dealer_skipped = False

player_1_card_1 = randint(2, 11)
player_1_card_2 = randint(2, 11)
player_1_current_hand = player_1_card_1 + player_1_card_2
print(f'Player was dealt {player_1_card_1} and {player_1_card_2} with Total of {player_1_current_hand}.')

bot_1_card_1 = randint(2, 11)
bot_1_card_2 = randint(2, 11)
bot_1_current_hand = bot_1_card_1 + bot_1_card_2
print(f'Bot 1 was dealt {bot_1_card_1} and {bot_1_card_2} with Total of {bot_1_current_hand}.')

bot_2_card_1 = randint(2, 11)
bot_2_card_2 = randint(2, 11)
bot_2_current_hand = bot_2_card_1 + bot_2_card_2
print(f'Bot 2 was dealt {bot_2_card_1} and {bot_2_card_2} with Total of {bot_2_current_hand}.')

dealer_card_1 = randint(2, 11)
dealer_card_2 = randint(2, 11)
dealer_current_hand = dealer_card_1 + dealer_card_2
print(f'Dealer was dealt {dealer_card_1} and {dealer_card_2} with Total of {dealer_current_hand}.')

while game_in_progress:

    if dealer_current_hand == BLACK_JACK:

        game_in_progress = False
        print(f'Black JACK! Dealer wins with cards {dealer_card_1} and {dealer_card_2}!')
        break

    if dealer_current_hand > BLACK_JACK:

        game_in_progress = False
        print(f'Dealer Lost and should be Punished (some evil emoji appears here!) All Players won!')
        break

    while player_turn:

        if player_1_current_hand > BLACK_JACK:

            player_turn = False
            print(f'Player lost with score {player_1_current_hand}.')

        if player_1_current_hand == BLACK_JACK:

            player_turn = False
            print(f'Player won with score {player_1_current_hand}!')

        if player_1_current_hand < BLACK_JACK:

            player_choice = input('Do you want to \'Pick\' or to \'Skip\'?\n')

            if player_choice == 'Pick':

                added_card = randint(2, 11)
                print(f'Player got {added_card}.')
                player_1_current_hand += added_card
                print(f'Player\'s current hand is {player_1_current_hand}.')

            elif player_choice == 'Skip':
                print('Player has Skipped and Turn is passed to Bot 1.')
                player_turn = False
                player_skipped = True

    while bot_1_turn:

        if bot_1_current_hand > BLACK_JACK:
            bot_1_turn = False
            print(f'Bot 1 lost with score {bot_1_current_hand}.')
            break

        if bot_1_current_hand == BLACK_JACK:
            bot_1_turn = False
            print(f'Bot 1 won with score {bot_1_current_hand}!')

        if bot_1_current_hand < 10:

            added_card = randint(2, 11)
            print(f'Bot 1 got {added_card}.')
            bot_1_current_hand += added_card
            print(f'Bot 1 current hand is {bot_1_current_hand}.')

        elif bot_1_current_hand < 15:

            pick_card_probability = randint(0, 1)
            #print(f'Current Bot 1 card probability equals {pick_card_probability}')

            if pick_card_probability == 0:

                bot_1_skipped = True
                bot_1_turn = False
                print(f'Bot 1 has Skipped and Turn is passed to Bot 2.')
                

            else:
                added_card = randint(2, 11)
                print(f'Bot 1 got {added_card}')
                bot_1_current_hand += added_card
                print(f'Bot 1 current hand is {bot_1_current_hand}.')

        else:
            print(f'Bot 1 has Skipped and Turn is passed to Bot 2.')
            bot_1_skipped = True
            bot_1_turn = False

    while bot_2_turn:

        if bot_2_current_hand > BLACK_JACK:

            bot_2_turn = False
            bot_2_skipped = False            
            print(f'Bot 2 lost with score {bot_2_current_hand}.')
            break

        if bot_2_current_hand == BLACK_JACK:

            bot_2_turn = False
            bot_2_skipped = False 
            print(f'Bot 2 won with score {bot_2_current_hand}.')

        if bot_2_current_hand < 10:

            added_card = randint(2, 11)
            print(f'Bot 2 got {added_card}')
            bot_2_current_hand += added_card
            print(f'Bot 2 current hand is {bot_2_current_hand}.')

        elif bot_2_current_hand < 15:

            pick_card_probability = randint(0, 1)
            #print(f'Current Bot 2 card probability equals {pick_card_probability}')

            if pick_card_probability == 0:

                bot_2_skipped = True
                bot_2_turn = False
                print(f'Bot 2 has Skipped and Turn is passed to Dealer.')

            else:
                added_card = randint(2, 11)
                print(f'Bot 2 got {added_card}')
                bot_2_current_hand += added_card
                print(f'Bot 2 current hand is {bot_2_current_hand}.')

        else:
            print(f'Bot 2 has Skipped and Turn is passed to Dealer.')
            bot_2_skipped = True
            bot_2_turn = False

    while dealer_turn:

        if dealer_current_hand > BLACK_JACK:

            dealer_turn = False
            game_in_progress = False
            print(f'Dealer Lost and should be Punished (some evil emoji appears here!) All Players won!')
            break

        elif dealer_current_hand < 10:

            added_card = randint(2, 11)
            print(f'Dealer got {added_card}.')
            dealer_current_hand += added_card
            print(f'Dealer\'s current hand is {dealer_current_hand}.')

        elif dealer_current_hand < 15:

            pick_card_probability = randint(0, 1)
            #print(f'Current Dealer card probability equals {pick_card_probability}')

            if pick_card_probability == 0:

                dealer_skipped = True
                dealer_turn = False

            else:
                added_card = randint(2, 11)
                print(f'Dealer got {added_card}')
                dealer_current_hand += added_card
                print(f'Dealer\'s current hand is {dealer_current_hand}.')

        else:
            print('Dealer has Skipped. We are about to find the winner...')
            dealer_turn = False

    if player_skipped == True and dealer_current_hand >= player_1_current_hand:
        print(f'Dealer won over Player with hand {dealer_current_hand}\nagainst {player_1_current_hand}!')

    elif player_skipped == True and dealer_current_hand <= player_1_current_hand:
        print(f'Player won over Dealer with hand {player_1_current_hand}\nagainst {dealer_current_hand}!')
        

    if bot_1_skipped == True and dealer_current_hand >= bot_1_current_hand:
        print(f'Dealer won over Bot 1 with hand {dealer_current_hand}\nagainst {bot_1_current_hand}!')
        

    elif bot_1_skipped == True and dealer_current_hand <= bot_1_current_hand:
        print(f'Bot 1 won over Dealer with hand {bot_1_current_hand}\nagainst {dealer_current_hand}!')
        

    if bot_2_skipped == True and dealer_current_hand >= bot_2_current_hand:
        print(f'Dealer won over Bot 2 with hand {dealer_current_hand}\nagainst {bot_2_current_hand}!')
        

    elif bot_2_skipped == True and dealer_current_hand <= bot_2_current_hand:
        print(f'Bot 2 won over Dealer with hand {bot_2_current_hand}\nagainst {dealer_current_hand}!')

    break
