# Try to implement with the first argument by default

def range_(end, step=1):

    range_list = []
    i = start

    while i < end:

        range_list.append(i)
        i += step

    return range_list


print(range_(0, 5))
