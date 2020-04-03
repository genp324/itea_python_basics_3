def sort_by_len(element):
    return len(element)


list_to_sort = ['ab', 'abc', 'a']
# ['a', 'ab', 'abc']
# ['abc', 'ab', 'a']
list_to_sort.sort(key=sort_by_len)
print(list_to_sort)
