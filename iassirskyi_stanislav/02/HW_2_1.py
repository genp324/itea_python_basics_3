string = list(input(f'Enter a string with "x" and "o": '))

x_list = []
o_list = []

for i in string:
    if i == 'x' or i == 'X':
        x_list.append(i)
    elif i == 'o' or i == 'O' :
        o_list.append(i)

if len(x_list) == len(o_list):
    print('True')
else:
    print('False')




    


    


    
