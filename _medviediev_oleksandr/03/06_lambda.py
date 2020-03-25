'''
def do_power(n, power):
    return n ** power


do_power = lambda n, power: n ** power
print(do_power(2, 3))
'''

def do_power(power):

    lambda_power = lambda number: number ** power
    
    return lambda_power


do_power_two = do_power(2)
do_power_three = do_power(3)

print(do_power_two(2))
print(do_power_three(2))
