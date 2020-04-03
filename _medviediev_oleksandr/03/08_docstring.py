def func_for_docstring(x, y):
    """
    This is a function to demonstrate docstring
    :param x: x is a number to represent blablabla
    :param y: y is a number to represent blablablabla
    :type x: int
    :type y: int
    :return: x plus y
    :rtype: int
    """
    return x + y


print(func_for_docstring.__doc__)
