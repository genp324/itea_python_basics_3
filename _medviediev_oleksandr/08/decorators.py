import time


def time_decorator(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()
        
        func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(execution_time)

    return wrapper
