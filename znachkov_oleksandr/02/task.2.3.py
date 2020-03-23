'''

Given an array, find the int that appears an odd number of times. There will always be only one integer that appears an odd number of times.

Examples:

list: [1, 2, 3, 1, 3, 2, 1]
output: 1

'''

list_num = [0,0,0,0,0]
counter = [0,0,0,0,0,0,0,0,0,0]

for index in range(len(list_num)):
    list_num[index] = int (input ("Enter number in the list:"))

for index in range(len(list_num)):
    counter[list_num[index]] += 1

for index in range(len(counter)):
    if counter[index] % 2 != 0:
        print (index)
        break
