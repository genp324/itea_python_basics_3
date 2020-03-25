my_list = [1, 2, 3, 1, 2, 3, 1]
length = len(my_list)

for i in range(0, length):
    number = 0
    for j in range(0, length):
        if my_list[i] == my_list[j]:
            number+=1

if(number % 2 != 0):
    print(my_list[i])
        
