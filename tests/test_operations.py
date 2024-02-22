'''Testing operations.py'''

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

@pytest.fixture
def setup_calculations():
    '''Setup calculations for testing'''
    arg_a = Decimal('10')
    arg_b = Decimal('5')
    operation = divide
    expected = Decimal('2')
    return arg_a, arg_b, operation, expected

def test_operation(setup_calculations):
    '''Testing various operations'''
    arg_a, arg_b, operation, expected = setup_calculations
    calculation = Calculation.create(arg_a, arg_b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Division by zero is not possible"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
