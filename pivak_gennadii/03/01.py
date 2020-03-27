

def implement_diff(list_a, list_b):
    """
    This is a function witch subtracts one list
    from another. It should remove all values from list_a,
    witch are present in list_b.
    :param list_a: list from witch will be remove values
    :param list_b: list witch will be remove from list_b
    :type list_a: list
    :type list_b: list
    :return: list_c list_a without values in list_b
    :rtype: list
    """
    list_c = []
    for _ in range(len(list_a)):
        if not list_a[_] in list_b:
            list_c.append(list_a[_])
    return list_c


#print(implement_diff.__doc__)
print(implement_diff([1, 2, 3, 4, 2, 3, 4],[2, 1, 4]))