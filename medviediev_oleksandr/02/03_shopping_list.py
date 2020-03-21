shopping_list = []

while True:

    new_element = input('What do you want to buy? ')
    shopping_list.append(new_element)

    one_more = input('One more? (y/n)')

    if one_more != 'y':
        break

print(shopping_list)

answer = input('Do you want to change something? (y/n)')

if answer == 'y':

    index_to_change = int(input('Index: '))
    new_item = input('New item: ')
    shopping_list[index_to_change] = new_item

print(shopping_list)
    
