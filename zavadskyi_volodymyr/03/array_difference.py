def difference(a, b):
    """
    This function subtracts one list from another and returns the result.
    :param a: a is a first list of numbers
    :param b: b is a second list of number, you want to substract from the first one
    :type a: list
    :type b: list
    :return: new list with substracted numbers
    :rtype: list
    """
    new_list = []
    
    for i in range(len(a)):
            if not(a[i] in b):
                new_list.append(a[i])

    return new_list


print(difference([1, 2, 3, 4, 5], [1, 3, 4]))

