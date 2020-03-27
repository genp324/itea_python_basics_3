

def remove_duplicates(a, b):
    """
    This function removes duplicated values from 2 provided lists
    :param a: Entry list 1
    :param b: Entry list 2
    :type a: list
    :type b: list
    :return: List of unique values
    :rtype: list
    """

    unique_list = []

    for i in a:

        counter = 0

        for j in b:

            if i == j:
                counter += 1

        if counter == 0:
            unique_list.append(i)

    return unique_list


c = remove_duplicates([1, 2], [1])
print(f'Unique values from example 1 are {c}')

d = remove_duplicates([1, 2, 2, 2, 3], [2])
print(f'Unique values from example 2 are {d}')