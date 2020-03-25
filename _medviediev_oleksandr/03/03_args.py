# ax + b = c
'''
def solve_linear_equation(b, c=1, a=2):

    x = (c - b) / a

    return x


number_three = 3 + 1

x = solve_linear_equation(1, 2, 3)
print(x)
'''
# x = solve_linear_equation(number_three, c=number_three, b=3)
# print(x)

# x = solve_linear_equation(3)
# print(x)

def solve_linear_equation(a, b, *args):

    print(a, b)
    for i in args:
        print(i)

    print(type(args))

    return args


x = solve_linear_equation(1, 'a', 3, 7123, [1, 'as', True], 192531, 1, 2, 3)
print(x)
