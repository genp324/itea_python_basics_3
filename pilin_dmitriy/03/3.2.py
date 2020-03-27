list_seq=(1,2,3,4,5)
b,c= 1,1


def simple_map(func,list_seq,*args):
    """
    :param arg1: function name
    :param arg2: iterable sequence list
    :param arg3: custom numbers of parameters
    :type arg1: function
    :type arg2: list
    :type arg3: int
    :return: return a list of the results of a function executed a specified number of times
    :rtype: return list
    """
    result_list = []
    
    for seq in list_seq:
       result_list.append(func(seq,*args))
    
    return result_list


def sum_calc(a,b,c):
    """
    :param arg1: value from iterable list
    :type arg1-3: int
    :return: return a the sum of three objects
    :rtype: int
    """
    return a + b + c


result = simple_map(sum_calc,list_seq,b,c) 
print (result)

result = simple_map(lambda sum: sum + b + c, list_seq)
print (result)


