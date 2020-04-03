#Variant 1

string_list = ()
len_string = 0
string_reverse = []
count_reverse = 0

string_list = list(input('input string '))
len_string = len(string_list)
string_reverse = list(string_list)
#print(string_reverse)

for i in range(len_string):
    count_reverse = len_string-i
    string_reverse[count_reverse-1] = string_list[i]
#    print(string_list[i])
#    print(count_reverse)
#print(string_reverse)

for i in range(len_string):
    print(string_reverse[i], end='')
print('')

#Variant 2

string_list = ()
len_string = 0

string_list = list(input('input string '))
len_string = len(string_list)
stop = (len_string + 1) * (-1)

for i in range(-1, stop, -1):
    print(string_list[i], end='')