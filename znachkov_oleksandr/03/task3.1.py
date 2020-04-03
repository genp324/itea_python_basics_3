from random import randint


ELEMENTS = 5 
HIGHLIMIT = 10

exclusion_list = [4,2]

def array_diff(source_list):
    print ("souerce list:", source_list)
    print ("exclusion list:", exclusion_list)
    #print (exclusion_list)
    return [ elem for elem in source_list if not elem in exclusion_list]

source_list = lambda listsize, upper : [randint(0, upper) for index in range (listsize)]

print ("result:", array_diff(source_list(ELEMENTS, HIGHLIMIT)))
