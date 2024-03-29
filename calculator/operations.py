'''Operations file, where all the calculator operations are listed'''

def add(arg_a,arg_b):
    '''adds the given arguments'''
    return arg_a + arg_b

def subtract(arg_a,arg_b):
    '''Subtracts the given arguments'''
    return arg_a - arg_b

def multiply(arg_a,arg_b):
    '''Multiplies the given arguments'''
    return arg_a * arg_b

def divide(arg_a,arg_b):
    '''Divides the given arguments'''

    if arg_b == 0:
        raise ValueError("Division by zero is not possible")
    return arg_a / arg_b
