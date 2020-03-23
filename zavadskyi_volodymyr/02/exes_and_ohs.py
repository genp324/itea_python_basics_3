'''
my_list = list(input("Enter some letters: "))
length = len(my_list)

x_count = 0
o_count = 0

for i in range(0, length):
    if my_list[i] == 'x' or my_list[i] == 'X':
        x_count += 1
    elif my_list[i] == 'o' or my_list[i] == 'O':
        o_count += 1
    
print("Number of x`s is", x_count)
print("Number of o`s is", o_count)
print(x_count == o_count)

'''

my_list = list(input("Enter some letters: "))

x_count = 0
o_count = 0

for i in range(0, len(my_list)):
    if my_list[i] == 'x' or my_list[i] == 'X':
        x_count += 1
    elif my_list[i] == 'o' or my_list[i] == 'O':
        o_count += 1
    
print(x_count == o_count)
        

