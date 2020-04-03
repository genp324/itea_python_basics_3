def filter_(func, some_list):
    """
    Work with 1 list of arguments
    :param func: function that you want to use
    :param some_list: arguments which you use in function
    :type func: Function
    :type some_list: list
    :return: create a list of elements for which a function returns true
    :rtype: list
    """
    
    result = []

    for arg in some_list:
        if func(arg):
            result.append(arg)
            
    return result


test_1 = filter_(lambda x: x % 2, [4, 5, 6, 7, 8, 9, 10])
print(test_1)
test_2 = filter_(lambda x: x % 2 == 0, [4, 5, 6, 7, 8, 9, 10])
print(test_2)
