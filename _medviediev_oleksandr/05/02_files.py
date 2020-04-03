# file = open('sample_text.txt', 'w')

# print(file.name)
# print(file.closed)

# text = file.read()
'''
text = file.readline()
print(text)
text = file.readline()
print(text)


for line in file.readlines():
    print(line + '123')

text = ['ASD', 'asd']

file.write(str(text))

file.close()
'''
with open('sample_text.txt', 'r') as file:
    text = file.read()

print(text)

# print(file.closed)
