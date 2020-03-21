my_list = [1, 2, 3, 'aasd']

for i in range(len(my_list)):

    print(f'Before {my_list[i]}')

    if my_list[i] == 2:
        my_list[i] = 3

    print(f'After {my_list[i]}')
