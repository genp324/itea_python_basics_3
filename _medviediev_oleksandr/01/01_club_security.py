MAX_ANSWERS = 10
MAX_VISITORS = 3

is_opened = True

answers = 0
visitors = 0


while is_opened:
    
    if answers >= MAX_ANSWERS:
        is_opened = False
        
    if visitors >= MAX_VISITORS:
        break

    answers += 1
    
    car = input('What is your car? ')
    
    if car != 'BMW':
        
        print('Sorry, you are not allowed')
        continue
    
    age = int(input('How old are you? '))
    
    if age > 80:

        money_amount = int(input('How much? '))

        if money_amount > 5:

            visitors += 1
            print('Are you ok?')
            print(f'Oh... {money_amount} bucks... You are welcome')

    elif age > 21:

        visitors += 1
        print('Welcome')

    elif age == 21:

        visitors += 1
        print('You are just in time')

    elif age < 10:

        print('Where are your parents?')

    else:

        print('Sorry, you are too young')


print('Sorry, we are closed.')
