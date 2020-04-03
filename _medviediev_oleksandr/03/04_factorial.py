def factorial(n):

    # n += 1
    factorial = 1

    for i in range(2, n + 1):
        factorial *= i

    return factorial


print(factorial(3))
print(factorial(5))
print(factorial(7))
