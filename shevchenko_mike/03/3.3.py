# print('Original function "filter"')
list_one = [1, -2, 3, 4, -5]

adds = list(filter((lambda x: x % 2), list_one))
positive_numbers = list(filter((lambda x: x>0), list_one))
print(adds)
print("")
print(positive_numbers)
