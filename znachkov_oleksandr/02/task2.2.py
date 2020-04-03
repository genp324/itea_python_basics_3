'''
Reverse a string

Examples:

input: "Hello"
output: "olleH"
'''

print ("Solution 1:")
str_input = input ("Input string for revers:")
str_reverse = []

for index in range (len(str_input)-1, -1, -1):
    str_reverse.append(str_input[index])
    
print (str_reverse)


print ("Solution 2:")
str_input = input ("Input string for revers:")
str_reverse = [str_input[index] for index in range(len(str_input)-1, -1, -1)]

print (str_reverse)
