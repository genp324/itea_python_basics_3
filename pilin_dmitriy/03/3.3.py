

def simple_filter(func,list_seq):
    """
    :param arg1: function name
    :param arg2: iterable sequence list
    :type arg1: function
    :type arg2: list
    :return: return 'True' list of elements for which a function returns  
    :rtype: return list
    """
    result_list=[]
    for i in list_seq:
        func_result = func(i)
        if func_result :
            result_list.append(i)
    return result_list


def odd_func(x):

    if x%2 == 0:
        return True
    else:
        return False
    

def less_zero_func(x):
    return x < 0

def bigger_zero_func(x):
    return x > 0


list_seq=(0,1,2,3,4,5,6,7,8,9)

result = simple_filter(odd_func,list_seq) 
print (result)

fltrObj=simple_filter(lambda x: x%2==0, list_seq)
print(list(fltrObj))

result = simple_filter(less_zero_func, range(-5,5)) 
print (result)

less_than_zero = list(simple_filter(lambda x: x < 0, range(-5, 5)))
print(less_than_zero)

result = simple_filter(bigger_zero_func, range(-5,5)) 
print (result)

bigger_than_zero = list(simple_filter(lambda x: x > 0, range(-5, 5)))
print(bigger_than_zero)

print("-----------")







