while True:
    
    name = input('Enter your name: ')

    if not name.isalpha():
        
        try:
            raise ValueError('Name should consist of letters only')
        except ValueError as error:
            print(error)
            continue

    break

print('OK')
