def custom_generator():
    # return [1, 2, 3, 4]
    yield 1
    yield 2
    yield 3
    yield 4


for i in custom_generator(): 
    print(i)


# Operators overriding
class Vector2D:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, other):

        return Vector2D(self.x + other.x, self.y + other.y)


a = Vector2D(2, 4)
b = Vector2D(5, 6)

c = a + b
