check_list = list(input ('Add list:\n'))
diff_list = list(input("Enter diff:\n"))



def array_diff(check_list, diff_list):
    """
    :param x: list of numbers to diff
    :param y: diff number
    :type x: type list
    :type y: type list
    :return: returning an list of values ​​after checking if the diff value is in the checked source list. 
    :rtype: return type list
    """
    result_list=[]

    for i in check_list:

        if i != diff_list[0]:
            result_list.append(i)
    return result_list


result=array_diff(check_list, diff_list)

print(result)