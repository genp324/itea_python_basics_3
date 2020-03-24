print('\nFirst example ')

text = list(input('Type string: ') )

num_o = 0
num_x = 0

for text in text :
    if text == 'o' or text == 'O':
        num_o += 1

    elif text == 'x' or text == 'X':
        num_x += 1

if num_o == num_x:
    print(True)

else:
    print(False)


print('\nSecond example ')

text_str = input('Type string: ')

check_o = [text_str for text_str in text_str if text_str == 'o' or text_str == 'O']
check_x = [text_str for text_str in text_str if text_str == 'x' or text_str == 'x']

print(len(check_o) == len(check_x))