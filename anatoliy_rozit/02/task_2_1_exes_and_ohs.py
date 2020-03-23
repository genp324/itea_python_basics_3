# The only way I can come up with at the moment

user_entered_text = input('Enter value to see if it has the same\namount of \'x\'s and \'o\'s: ')

count_of_o = 0

count_of_x = 0

for letter in user_entered_text:

    if letter == 'o' or letter == 'O':
        count_of_o += 1

    if letter == 'x' or letter == 'X':
        count_of_x += 1

if count_of_o == count_of_x:
    print(True)

else:
    print(False)

'''
1. It is a shame we cannot use at least lower() to avoid comparing upper and lower case letters.
It would simplify "if" condition.
2. It is a pitty we cannot use .count(). It would drastically decrease the volume of code (even though
it is a fairly small task it should not deserve that many characters to be written).
'''
