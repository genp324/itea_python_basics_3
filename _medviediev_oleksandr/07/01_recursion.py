'''
x = 2
n = 4

2 ** 4
x * x ** (n - 1)


2 ** 4 = 2 * 2 * 2 * 2 * 1
2 ** 3 = 2 * 2 * 2 * 1
2 ** 2 = 2 * 2 * 1
2 ** 1 = 2 * 1
2 ** 0 = 1
'''
def power(x, n):

    if n == 0:
        return 1

    return x * power(x, n - 1)

'''
power(2, 4) = 2 * power(2, 3)
power(2, 3) = 2 * power(2, 2)
power(2, 2) = 2 * power(2, 1)
power(2, 1) = 2 * power(2, 0)
power(2, 0) = 1
'''

print(power(3, 12))
