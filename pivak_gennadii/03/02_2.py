def map_custom (func, *args):
    """
    This is a function witch must be like original Python function map.
    :param func: Required. The function to execute for each item
    :param *args: Required. A sequence params coma separeted or as a list.
    :type func: str
    :type *args: list
    :return: list of results
    :rtype: list
    """
    result = []
    if not len(args) == 1:
        for i in range(len(args)):
            result.append(func(args[i]))
    else:
        for arg in args:
            for i in range(len(arg)):
#                print(arg[i])
                result.append(func(arg[i]))
    return result


#1 attemt
def myfunc(n):
    return len(n)


#print(map_custom.__doc__)
x = list(map_custom(myfunc, ('apple', 'mango', 'banana')))
print(x)


#2 attemt
def myfunc(n):
    var = n * n
    return var


x = list(map_custom(myfunc, (33, 444, 5566)))
print(x)

#3 attemt
calc = list(map_custom(lambda x: x ** 2, 1, 2, 3, 4, 8))
print(calc)


#4 attemt
def to_upper_case(s):
    return str(s).upper()


map_iterator = map_custom(to_upper_case, (1, 'a', 'abc'))
print(map_iterator)

