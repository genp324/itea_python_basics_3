def morethen5 (number):
    if number > 5:
        return True
    else:
        return False


def ifodd (number):
    if number % 2:
        return False 
    else:
        return True


def filterx (func, iterable):
    retlist = []
    for elem in iterable:
        if func(elem):
            retlist.append(elem)
    return retlist


list_my = [1,2,3,4,5,7,8,9,10]
print (filterx (morethen5, list_my))
print (filterx (ifodd, list_my))
