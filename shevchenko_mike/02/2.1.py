#approach_1

print("approach_1")
print('')

chars = ('ooxx')

print('We have - ', len(chars),  'symbols')
print('symbol - "o" -', chars.count('o'))
print('symbol - "x" -', chars.count('x'))

if chars.count('x') != chars.count ('o'):
    print(False)
    print('')

if chars.count('x') == chars.count('o'):
    print(True)
    print('')

#approach_2
print("approach_2")
print('')

chars_2 = ('xooxx')

print('')
print('We have - ', len(chars_2),  'symbols')
print('symbol - "o" -', chars_2.count('o'))
print('symbol - "x" -', chars_2.count('x'))

if chars_2.count('x') == chars_2.count('o'):
    print(True)
    print('')

if chars_2.count('x') != chars_2.count('o'):
    print(False)
    print('')
'''
#approach_3
print("approach_3")
print('')

chars_3 = ('ooxXm')
count = {}


print('')
print('We have - ', len(chars_3),  'symbols')
print('symbol - "o" -', chars_2.count('o'))
print('symbol - "x" -', chars_2.count('x'))
print('symbol - "X" -', chars_2.count('X'))
print('symbol - "m" -', chars_2.count('m'))


input: "ooxXm"
output: True
'''
#approach_4
print("approach_4")
print('')

chars_4 = ('zpzpzpp')
print('We have - ', len(chars_4),  'symbols')
print('symbol - "o" -', chars_4.count('o'))
print('symbol - "x" -', chars_4.count('x'))
print('symbol - "z" -', chars_4.count('z'))
print('symbol - "p" -', chars_4.count('p'))


line_1 = int(input('enter a string: for example "zpzpzpp"'))
print(True)

if chars_4 == chars_2.count('o'):
    if chars_4 != {'x'}:
        print ('Kolobok')


print(True)
print('')


"""
True when no 'x' and 'o' is present
input: "zpzpzpp"
output: True
"""
