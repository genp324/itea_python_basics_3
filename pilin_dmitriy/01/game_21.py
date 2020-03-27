from random import randint


level_check = True

while level_check:

    LEVEL = int(input('Welcome to \"Game 21\"\nChose your level: (1 - single player; 2 - with one bot; 3 - with two bots)\n'))

    if (1 <= LEVEL <= 3 ):

        print('Let\'s Play 21!')
        level_check = False

    else:
        print('Try better ')

if LEVEL >= 1:
    
    card_1_deal = randint(2,11)
 
    card_2_deal = randint(2,11)
 
    player_ace_win = False
 
    player_win = False
 
    if card_1_deal == 11 and card_2_deal == 11:
 
        print ('Winner. You got 2 aces')
        player_ace_win = True
        player_deal = 21
 
    else :
 
        player_deal = card_1_deal + card_2_deal
        print(f' First card: {card_1_deal}  Second card: {card_2_deal}  Total Deal: {player_deal}')
 
        if player_deal == 21:
 
            print ('Congradulations. You got 21')
            player_win = True
 
    while player_deal <= 20:
 
        more_card = input('One more card? (type y or n) \n')
 
        if more_card == 'n' or more_card == 'N':
 
            player_win = False
            break
 
        elif more_card == 'y' or more_card == 'Y':
 
            card_deal = randint(2,11)
            player_deal += card_deal
            print(f'New card: {card_deal}  Total Deal: {player_deal}')
 
            if player_deal == 21:
 
                player_win = True
                
            elif player_deal > 21:
 
                player_win = False

#bot 1 step

if LEVEL >= 2 and player_win == False and player_ace_win==False:

    print ('---Let\'s play with Bot 1---')
    card_1_deal=randint(2,11)
    card_2_deal=randint(2,11)
    bot1_ace_win = False
    bot1_win = False

    if card_1_deal == 11 and card_2_deal == 11:

        print ('Winner. You got 2 aces')
        bot1_ace_win = True
        bot1_deal = 21

    else:

        bot1_deal = card_1_deal + card_2_deal

        if bot1_deal == 21:

            print ('bot 1 has 21 and WIN!')
            bot1_win = True

        print(f'First card: {card_1_deal}  Second card: {card_2_deal}  Total Deal: {bot1_deal}')

# draw more cards

        while bot1_deal <=21:

            risky_deal = randint(0,1)

            if 2 < bot1_deal < 20 and risky_deal == 1 and bot1_deal < 21:

                print(f'Risk {risky_deal}. Bot1 want one more card')
                card_deal = randint(2,11)
                bot1_deal += card_deal
                print(f'New bot1 card: {card_deal}  Total bot1 Deal: {bot1_deal}')

            elif 19 < bot1_deal < 22:

                print(f'Bot1 say: \'Enough!\' with {bot1_deal}')
                break

        if bot1_deal == 21:

            bot1_win = True

        elif bot1_deal > 21:

            bot1_win = False

        elif bot1_deal < 20:

            bot1_win = False

#bot 2 step         

if LEVEL == 3 and player_win == False and bot1_win == False and player_ace_win==False and bot1_ace_win == False:

    print ('---Let\'s play with Bot 2---')
    card_1_deal = randint(2,11)
    card_2_deal = randint(2,11)
    bot2_ace_win = False
    bot1_win = False

    if card_1_deal == 11 and card_2_deal == 11:

        print ('Winner. You got 2 aces')
        bot2_ace_win = True
        bot2_deal = 21

    else:

        bot2_deal = card_1_deal + card_2_deal

        if bot2_deal == 20:

            print ('Bot2 1 has 21 and WIN!')
            bot2_win = True

        print(f'First card: {card_1_deal}  Second card: {card_2_deal}  Total Deal: {bot2_deal}')

# draw more cards

        while bot2_deal <= 21:

            risky_deal = randint(0,1)

            if 2 < bot2_deal < 20 and risky_deal == 1 and bot2_deal < 21:

                print(f'Risk {risky_deal}. Bot1 want one more card')
                card_deal = randint(2,11)
                bot2_deal += card_deal
                print(f'New Bot 2 card: {card_deal}  Total bot1 Deal: {bot2_deal}')

            elif 19 < bot2_deal < 22:

                print(f'Bot 2 say: \'Enough!\' with {bot2_deal}')
                break

        if bot2_deal == 21:

            bot2_win = True

        elif bot2_deal > 21:

            bot1_win = False

        elif bot2_deal < 20:

            bot1_win = False
#
#paranoid  results verification 
# 
print(f'\nResults:\n')

if LEVEL == 1 and player_ace_win==True:

    print (f'Player win with 2 Aces')

elif LEVEL == 2 and bot1_ace_win==True:

    print (f'Bot1 win with 2 Aces')

elif LEVEL == 3 and bot2_ace_win==True:

    print (f'Bot2 win with 2 Aces')

if LEVEL == 1 and player_deal <=20:

    print (f'Player got {player_deal} Points')

elif LEVEL == 1 and player_deal == 21:

    print (f'Player got {player_deal} And WIN')

elif LEVEL == 1 and player_deal > 21:

    print (f'Player got {player_deal} And LOST')

elif LEVEL == 2 :

    if player_deal == 21 or (bot1_deal > 21 and player_deal <= 20):

        print (f'Player win with {bot1_deal}')

    elif bot1_deal == 21 or(player_deal > 21 and bot1_deal <= 20):

        print (f'Bot 1 win with {bot1_deal}')

    elif player_deal == bot1_deal and player_deal <=21:

        print(f'Player with {player_deal} and  Bot1 with {bot1_deal} is draw.')

    elif player_deal <= 21 and player_deal > bot1_deal :
        
        print (f'Player win with {player_deal} and Bot 1 lost with {bot1_deal}')

    else:

        print (f'Bot 1 win with {bot1_deal} and Player lost with {player_deal}')

if LEVEL == 3 :

#    check_player_to_bot1_win = player_deal > bot1_deal 
#    check_player_to_bot2_win = player_deal > bot2_deal
#    check_bot1_to_bot2_win = bot1_deal > bot2_deal

    if player_deal > 21 and bot1_deal > 21 and bot2_deal > 21:
 
        print ('No winner')
 
    elif player_deal == bot1_deal == bot2_deal and player_deal <= 21:

        print('WOW. Super draw')

    elif player_deal <= 21 and player_deal > bot1_deal == True and player_deal > bot2_deal == True :

        print(f'Player win with {player_deal}. Bot1: {bot1_deal}. Bot2:{bot1_deal}')

    elif player_deal <= 21 and player_deal > bot1_deal == False and player_deal == bot1_deal and player_deal >= bot2_deal :

        print(f'Player  with {player_deal} and  Bot1 with {bot1_deal} is draw.')

    elif player_deal <= 21 and player_deal > bot1_deal == False and player_deal == bot2_deal and player_deal >= bot1_deal:

        print(f'Player  with {player_deal} and  Bot2 with {bot2_deal} is draw.')

    elif bot1_deal <= 21 and bot1_deal > bot2_deal == True:

        print(f'Bot1 win with {bot1_deal}. Player: {player_deal}. Bot2:{bot2_deal}')

    elif bot1_deal <= 21 and bot2_deal > 21 and player_deal > 21 :

        print (f'Bot1 win with {bot1_deal}. Player: {player_deal}. Bot2:{bot2_deal}')

    elif bot2_deal <= 21 and bot1_deal > 21 and player_deal > 21 :

        print (f'Bot2 win with {bot1_deal}. Player: {player_deal}. Bot1:{bot2_deal}')
    
    elif player_deal <= 21 and bot2_deal > 21 and bot1_deal > 21 :

        print (f'Player win with {player_deal}. Bot1: {bot1_deal}. Bot2:{bot2_deal}')
    
    elif bot1_deal <= 21 and bot1_deal > bot2_deal == False and bot1_deal == bot2_deal:

        print(f'Bot1  with {bot1_deal} and Bot2:{bot2_deal} is draw')

    elif bot2_deal <= 21 :

        print(f'Bot2 win with {bot2_deal}. Player: {player_deal}. Bot1:{bot1_deal}')
