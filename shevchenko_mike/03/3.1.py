"""  
    So, we have difference function, which subtracts one list from another a from b.
    The goal in this programm is to implement an difference function, which subtracts
    one list from another.
    :param python collection (list)
"""


a = [1,  3,  5, 6]
b = [4, 5, 6, 8, 9]
#or
#a = ([1,2],[1])
#b = ([1,2,2,2,3],[2])

def array_diff(a, b):
    new_list = []
    for i in a:
        if i not in b:
            new_list += [i]
    return new_list

print(array_diff(a, b))
        

