

def test_function( ):
"""
:param arg1: description
:param arg2: description
:type arg1: type
:type arg2: type
:return: return description
:rtype: return type
"""
pass

'''
filter(function, sequence)

filter(lambda x: x % 2, numbers)
'''
def simple_filter(func,list_seq):
    for i in list_seq:
        func_result = func(i)
        if i == func_result:
            return True
        else:
            return False




fltrObj=filter(lambda x: x%2==0, range(10))
print(list(fltrObj))