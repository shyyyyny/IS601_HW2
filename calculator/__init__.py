'''Calculator Class'''

from decimal import Decimal
from typing import Callable

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide



class Calculator:
    '''class structured with static methods'''

    @staticmethod
    def _perform_operation(arg_a, arg_b, operation) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(arg_a, arg_b, operation)
        Calculations.add_calculation(calculation)
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
    