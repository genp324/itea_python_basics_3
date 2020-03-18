# With numbers - wrong
PIN_CODE = 1234
MAX_ATTEMPTS = 3

attempts = 0


while True:

    user_pin = int(input('Please enter your pin: '))
    attempts += 1

    if 1 <= user_pin / 1000 < 10 and 1 <= user_pin / 100000 < 10:
        print('Pin code should be 4 or 6 symbols')
        continue

    if user_pin == PIN_CODE:
        print('Welcome')
        break
    else:
        print('Invalid pin code. Try again!')

    if attempts >= MAX_ATTEMPTS:
        print('Sorry. Your card was blocked.')
        break

# With string
'''
PIN_CODE = '1234'
MAX_ATTEMPTS = 3

attempts = 0


while True:

    user_pin = input('Please enter your pin: ')
    attempts += 1

    if len(user_pin) != 4 and len(user_pin) != 6:
        print('Pin code should be 4 or 6 symbols')
        continue

    if user_pin == PIN_CODE:
        print('Welcome')
        break
    else:
        print('Invalid pin code. Try again!')

    if attempts >= MAX_ATTEMPTS:
        print('Sorry. Your card was blocked.')
        break
'''
