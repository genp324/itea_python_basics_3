def map_(func, some_list):
    """
    Try to build a function like a origin map
    Its working with 1 list of arguments
    :param func: function that you want to use
    :param some_list: arguments which you use in function
    :type func: Function
    :type some_list: list
    :return: result in function
    :rtype: list
    """
    
    result = []
    
    for arg in some_list:
        result.append(func(arg))
        
    return result


def simple(a):
    return a + a


test_1 = map_(lambda x: x*2, [3, 2, 4, 5, 6])
test_2 = map_(simple, [1, 2, 3, 4])
print(test_1)
print(test_2)
