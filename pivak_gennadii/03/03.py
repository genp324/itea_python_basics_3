def filter_custom (func, arg):
    """
    This is a function witch must be like original Python function filter.
    :param func: Required. The function to execute for each item.
                 func has to return a Boolean value, i.e. either True or False
    :param arg: Required. A sequence as a list.
    :type func: str
    :type arg: list
    :return: list of results
    :rtype: list
    """
    result = []

    for i in range(len(arg)):
            if func(arg[i]):
                result.append(arg[i])
    return result

print(filter_custom.__doc__)

list_int = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
odd_numbers = list(filter_custom(lambda x: x % 2, list_int))
print(odd_numbers)

even_numbers = list(filter_custom(lambda x: x % 2 == 0, list_int))
print(even_numbers)
