array_2d = []

for i in range(8):

    row = []
    
    for j in range(8):
        row.append('| ')

    row.append('|')
    array_2d.append(row)
    
for row in array_2d:
    
    for element in row:
        print(element, end='')

    print('\n', end='')


'''
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
'''
