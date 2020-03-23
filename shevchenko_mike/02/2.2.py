
#approach_1 the most better!
print ('approach_1')
print('')

print('Hello')
word = 'Hello'[:: -1]

print(word)


#approach_2
print ('approach_2')
print('')

word_2 = 'Hello'
def reverse(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    print('reversed string is:',reversed_string)

string = input('enter a string:')
print('entered string', string)
reverse(string)


#approach_3
print ('approach_3')
print('')

print('')
print('Hello')

inputStr = 'Apple'
print(inputStr)
print(inputStr[-1::-1])

#approach_4
print ('approach_4')
print('')

inputStr = 'pear'
result = ''

for i in range(len(inputStr)-1, -1, -1):
    result = result  + inputStr[i]
print('')
print('pear')
print(result)    

