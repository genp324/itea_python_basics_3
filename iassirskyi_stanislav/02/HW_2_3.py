array = list(input('Enter the array: '))


for i in range(len(array)):
    check_array = []
            
    for j in range(len(array)):
        if array[i] == array[j]:
            check_array.append(array[i])
                
    if len(check_array) % 2 != 0 and len(check_array) > 1:
        n = check_array[0]

print(f'the int that appears an odd number of times: {n}')





    
        
        
