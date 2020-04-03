'''
# Try to use *args
def function(func, c, *args):
    return func(*args) + c


def calculate(a, b):
    return a * b


print(function(calculate, 1, 2, 3))
'''

# map(lambda x: x ** 2, [1, 2, 3])

def normalize(x):

    x = x.strip()
    x = x.lower()
    x = x.capitalize()

    return x


normalized_names = list(map(normalize, ['alEx    ', '  mAx', 'VASYA']))
print(normalized_names)
