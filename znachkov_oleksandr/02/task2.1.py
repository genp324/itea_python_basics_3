'''
Check to see if a string has the same amount of 'x's and 'o's. The string can contain any char.

Examples:

input: "ooxx"
output: True

input: "xooxx"
output: False

input: "ooxXm"
output: True

True when no 'x' and 'o' is present
input: "zpzpzpp"
output: True
'''
print ("Solution 1:")
searchstr = input ("Input string for search:")
xes = ous = 0

for letter in searchstr:
    if letter == 'x' or letter == 'X':
        xes+=1
    if letter == 'o' or letter == 'O':
        ous+=1
if xes == ous: 
    print ("True")
else:
    print ("False")

print ("Solution 2:")
searchstr = input ("Input string for search:")
xes = ous = 0

for index in range(len(searchstr)):
    if searchstr[index] == 'x' or searchstr[index] == 'X':
        xes+=1
    if searchstr[index] == 'o' or searchstr[index] == 'O':
        ous+=1
if xes == ous: 
    print ("True")
else:
    print ("False")
