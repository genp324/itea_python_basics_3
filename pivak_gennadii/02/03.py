#Variant 1

list_array = list(input('Input array digit (like this - 6675675) '))

for i in range(len(list_array)):
    count_element = 0
#    print(f'Search {list_array[i]}')
#    print(i)
    for j in range(len(list_array)):
        if list_array[i] == list_array[j] and i != j:
            count_element += 1
#            print(j)
    if not count_element % 2:
        break
print(f'Find! {list_array[i]}')

#Variant 2

len_array = 0

list_array = list(input('Input array digit (like this - 6675675) '))
len_array = len(list_array)

array_2d = []

for i in range(len_array) :

    row = []

    for j in range(len_array):
        if list_array[i] == list_array[j] and i != j and i not in array_2d:
            row.append(j)
    row.append(i)
    array_2d.append(row)
    if len(row) % 2:
        print(list_array[i])
        break
#print(array_2d)

#Variant 3


list_array = list(input('Input array digit (like this - 6675675) '))

transpose = [[1 if list_array[i] == list_array[j] else 0 for j in range(len(list_array))] for i in range(len(list_array))]
#print(transpose)

row_count = 0
element_sum = 0
for row in transpose:
#    print(row)
    for element in row:
        element_sum += element
#    print(element_sum)
    if element_sum % 2:
        print(f'Find! {list_array[row_count]}')
        break
    row_count += 1
    element_sum = 0