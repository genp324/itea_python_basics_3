def do_power_two(number):
    number **= 2 
    return number

def mapper (func, iterable):
    retlist = []
    for elem in iterable:
        retlist.append (func(elem))
    return retlist

list_my = [1,2,3,4,5]
print (mapper (do_power_two, list_my))
