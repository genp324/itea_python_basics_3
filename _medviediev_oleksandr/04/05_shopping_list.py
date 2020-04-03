def create_shopping_list(iterations):

    shopping_list = {}

    for _ in range(iterations):

        element = input('What to add? ')
        quantity = input('How many? ')

        if not quantity.isdigit():
            print('Should be integer')
            
        shopping_list[element] = quantity

    return shopping_list


def show_how_many(shopping_list):

    key = input('What to show? ')
    print(shopping_list[key])


iterations = int(input('How many elements? '))
shopping_list = create_shopping_list(iterations)
print(shopping_list)

show_how_many(shopping_list)
