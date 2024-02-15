'''Calculator Class'''

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
from typing import Callable


class Calculator:
    '''class structured with static methods, to perform calculator operations such as add, sub, multiply and divide
    from the operations.py file'''

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(arg_a, arg_b):
        '''uses the calculation class to create a calculation and '''
        return Calculator._perform_operation(arg_a, arg_b, add)

    @staticmethod
    def subtract(arg_a, arg_b):
        '''subtracts the given arguments'''
        return Calculator._perform_operation(arg_a, arg_b, subtract)

    @staticmethod
    def multiply(arg_a, arg_b):
        '''multiplies the given arguments'''
        return Calculator._perform_operation(arg_a, arg_b, multiply)

    @staticmethod
    def divide(arg_a, arg_b):
        '''divides the given arguments'''
        return Calculator._perform_operation(arg_a, arg_b, divide)