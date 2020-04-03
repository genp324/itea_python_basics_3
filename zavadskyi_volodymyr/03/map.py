def map_(func, args):
    """
    This is a function to demonstrate map function
    :param func: func is a function, you want to use for a list of arguments
    :param args: args is a list of arguments
    :type func: function
    :type args: list
    :return: new list with deformed arguments of using function
    :rtype: list
    """
    new_list = []
    
    for i in range(len(args)):
        new_list.append(func(args[i]))
    
    return new_list


def addition(n): 
    return n + n + n


print(map_(addition, [2, 2, 3, 4]))
print(map_(lambda x: x**2, [10, 2, 3]))
