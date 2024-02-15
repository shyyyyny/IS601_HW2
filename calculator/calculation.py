'''Calculation Class'''

class Calculation:
    '''defines a calculation class and initialized the operation along with arguments'''
    def __init__(self, arg_a, arg_b):
        self.arg_a = arg_a
        self.arg_b = arg_b
        self.operation = None

    @classmethod
    def create(cls, arg_a, arg_b, operation):
        '''Creates and instance of the class with operation to perform on the specified arguments'''
        instance = cls(arg_a, arg_b)
        instance.operation = operation
        return instance
    def perform(self):
        """Perform the stored calculation and return the result."""
        return self.operation(self.arg_a, self.arg_b)
    def get_result(self):
        '''returns the result of the operation specified on the arguments'''
        if self.operation is None:
            raise ValueError("listed operation cannot be found")
        return self.operation(self.arg_a, self.arg_b)
    