class MyException(Exception):
    pass


try:
    if True:
        raise MyException('My exception description')
except MyException as error:
    print(error)
