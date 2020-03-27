

def power(number):

    result = number * number

    return result


def my_map(function, some_list):
    """
    This is a custom map() function which can work with 1 function and 1 iterable list
    :param function: function name
    :param some_list: list of items to iter through
    :type function: function
    :type some_list: list
    :retun: List of values resulted from entered function
    :rtype: list
    """

    output = []

    for i in some_list:

        func_result = function(i)
        output.append(func_result)

    return output

result_1 = my_map(power, [1, 2, 3])
print(result_1)

result_2 = my_map(lambda x: x * 2, [1, 2, 3])
print(result_2)