from decorators import time_decorator


@time_decorator
def multiply(n, m):
    for i in range(100000000):
        pass


multiply(1, 2)




    
