from random import randint

#number = random.randint (2,11)
print("Let start to play game 21 points")

count_Players_1 = 0
P = 'Players_1'
count_Bot = 0
B = 'Bot'

Card_1 = randint(2,11)

Card_2 = randint(2,11)

Card_3 = randint(2,11)

Card_sum_Players_1 = Card_1 + Card_2
print('Players_1 ')
print('So, you  have points - ' + str(Card_1))
print('So, you  have points - ' + str(Card_2))
print('So, this is all your points - ' + str(Card_sum_Players_1))
print('')

if Card_sum_Players_1 < 21:
    count_Players_1 = 1

while count_Players_1:
    next_cards = input('You are take a new card - ?' '[ yes? / not?]')
    if next_cards == 'yes':
        Card_3 = randint(2, 11)
        Card_sum_Players_1 += Card_3
        print(f'next_cards {Card_3}')
        print('So, you  have point - ' + str(Card_sum_Players_1))

    if next_cards == 'not':
        print('So, you  have point - ' + str(Card_sum_Players_1))
        if Card_sum_Players_1 <= 21:
            print('You are win!')
        elif Card_sum_Players_1 > 21:
            print('Sorry, You are lose =(')
        break

    if Card_sum_Players_1 == 21:
        print ('You are win! You are lucky!!')
        break

    if Card_sum_Players_1 >= 18 and Card_sum_Players_1 <= 21:
        print('You are win! You  have point - ' + str(Card_sum_Players_1))
        break

    elif Card_sum_Players_1 > 21:
        print('Sorry, You are lose =(')
    elif Card_1 == 11 and Card_2 == 11:
        print('golden twenty one')

    if count_Players_1 > Card_sum_Players_1 or Card_sum_Players_1 > 21:
        if Card_sum_Players_1 > 21:
            print('Sorry, you have point - ' + str(Card_sum_Players_1))
        else:
            print('Game over!')
        break


print('Goodbye! :)')
