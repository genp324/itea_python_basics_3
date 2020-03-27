print('Approach_1')
print('map_original')
my_list = ['hello', "what`s up", 'good morning']
map_original = list(map(lambda x: x[:: -1], my_list))

print(map_original)
"""
    So, this is test function custom_map = map_original
    Firstly,the function  map_original we will use python collection (list),
    than function 'map', than function 'lambda'.
    Secondly, this is function custom_map return first latter in end words
    :param python collection (list)
    :param str.
    :param lambda.
"""
print('')
print('custom_map')
custom_map = [i[:: -1] for i in my_list]
print(custom_map)

#Approach_2
print('Approach_2')
print ('Enter numeral "For example: 1 76 33 5..."')
"""
    So, this Approach_2 to use function map.
    Firstly, you must to enter new numeral
    Secondly, this is function custom_map return first latter in end words
    :param python collection (list)
    :param int
    :param input()
    :param Python String split() Method
"""

def f(x):
    return x * 2

my_list_2 = list(map(int, input().split()))

print (my_list_2)