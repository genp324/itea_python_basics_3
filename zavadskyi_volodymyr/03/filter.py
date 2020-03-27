def filter_(func, args):
    """
    This is a function to demonstrate filter function
    :param func: func is a function, you want to use for a list of arguments
    :param args: args is a list of arguments
    :type func: function
    :type args: list
    :return: new list with deformed arguments of using function
    :rtype: list
    """
    new_list = []
    
    for i in range(len(args)):
       if func(args[i]) == True:
            new_list.append(args[i])
           
    return new_list


print(filter_(lambda x: x % 2, [9, 4, 2, 5, 10, 13, 17, 4]))




