#raw_list = list(input('Input raw int: '))

raw_list = [1, 2, 3, 1, 3, 2, 1]

clean_list = []

for n in raw_list:

    if [n, 0] not in clean_list:
        clean_list.append([n, 0])

for n in raw_list:

    index = 0

    for l in clean_list:

        count = l[1]
        number = l[0]

        if n == number:
            clean_list[index] = [number, count + 1]

        index = index + 1

for i in range(len(clean_list)):

    if  clean_list[i][1] % 2:
        print(f'The odd number is: {clean_list[i][0]}')

#--or--

result = [i for i in range(len(clean_list)) if clean_list[i][1] % 2]

for i in result:
    print(f'The odd number is: {clean_list[i][0]}')
    