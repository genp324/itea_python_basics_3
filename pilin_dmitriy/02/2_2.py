#text = list(input('Input string to reverse: '))

text = list('Hello')

print('\nFirst example ')

let_num = len(text) - 1

while let_num > -1 :

    print(text[let_num], end='')
    let_num -= 1

print('\nSecond example ')

for i in range(len(text) - 1, -1, -1):
    print(text[i],end='')

print('\nThird example')
     
new_text = []

for i in range(-1, -(len(text) + 1), -1):
    new_text.append(text[i])

for letter in new_text:
    print(letter, end = '')


# Not an example. Just a cheat sheet
'''
txt = "Hello World"[::-1]
print(txt)
'''