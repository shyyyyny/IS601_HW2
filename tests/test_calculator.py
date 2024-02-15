'''Calculator Tests'''
import pytest
from calculator import Calculator

def test_addition():
    '''Tests the addition'''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Tests the subtraction'''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Tests the multiplication'''     
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Tests the division'''      
    assert Calculator.divide(2,2) == 1

def test_zero_divide():
    '''Tests division by zero throws a value error'''
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
        