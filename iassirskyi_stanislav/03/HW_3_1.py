def compare_list(list_a, list_b):
    """
    The function, which subtracts one list from another
    :param list_a: first list which you want to compare
    :param list_b: values in this list will be compared with list_a
    :type list_a: list
    :type list_b: list
    :return: values in list_b will be deleted in list_a
    :rtype: list
    """
        
    diff_num = []
    
    for i in list_a:
        step = 0
        
        for j in list_b:
            if j == i:
                step += 1
    
        if step == 0:
            diff_num.append(i)
        
    return diff_num


list_a = list(input('Enter your first list: '))
list_b = list(input('Enter your second list: '))

print(compare_list(list_a, list_b))
