string = list(input('Enter a string and I revers it: '))

revers_list = []

revers = ''

index = len(string)

i = 0


while i < index:

    new_index = (index - 1) - i

    new_letter = string[new_index]
    
    revers_list.append(new_letter)
    i+=1

for l in revers_list:
    revers += l

print(revers)


    
