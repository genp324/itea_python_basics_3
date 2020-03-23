
my_list = ('1', '2', '3', '1', '3', '2', '1')

my_list_1 = [1, 2, 3, 1, 3, 2, 1]

number_one = 0
number_two = 0
number_three = 0

print('We have - ', len(my_list),  'symbols')
print('')
print('symbol - "1" -', my_list.count('1'))
print('symbol - "2" -', my_list.count('2'))
print('symbol - "3" -', my_list.count('3'))
print('')

for i in my_list:
    if i < 1:
        number_one += 1
    elif i < 2:
        number_two += 1
    elif i < 3:
        number_three += 1

print("1", my_list.count('1'))


list: [1, 2, 3, 1, 3, 2, 1]
output: 1




