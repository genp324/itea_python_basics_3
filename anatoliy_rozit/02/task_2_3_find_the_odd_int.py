# Current working approach
# 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 5

my_list = [1, 2, 3, 1, 3, 2, 1]

index_of_item_to_compare = 0

length_of_list = len(my_list)

index_of_next_item_to_compare = index_of_item_to_compare + 1

item_ocurrence = 0

while index_of_item_to_compare < length_of_list:

    if item_ocurrence % 2 == 0:
        print(my_list[index_of_item_to_compare - 1])

    while index_of_next_item_to_compare <= length_of_list:

        if my_list[index_of_item_to_compare] == my_list[index_of_next_item_to_compare <= length_of_list]:
            print(item_ocurrence)
            item_ocurrence += 1
            
            
        index_of_next_item_to_compare += 1

    index_of_item_to_compare += 1
    
    break


















