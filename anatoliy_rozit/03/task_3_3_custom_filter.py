

def return_odd_number(number):

    if number % 2 == 1:
        return True

    else:
        return False
   

def my_filter(function, list_of_numbers):

    """
    This is a custom filter() function which can work with 1 function and 1 iterable list
    :param function: function name
    :param list_of_numbers: list of items to iter through
    :type function: function
    :type list_of_numbers: list
    :retun: List of values resulted from entered function
    :rtype: list
    """

    filtered_list = []
    
    for i in list_of_numbers:

        if function(i) == True:
            filtered_list.append(i)

    return filtered_list


c = my_filter(return_odd_number, [5, 2, 7, 8, 9, 11, 12])
print(c)