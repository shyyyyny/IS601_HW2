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
        '''Raises a zero division error'''
        raise ValueError("cannot divide by 0")
    return arg_a / arg_b