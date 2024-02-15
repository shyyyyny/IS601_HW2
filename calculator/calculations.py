'''Calculations class'''

from typing import List

from calculator.calculation import Calculation

class Calculations:

    '''History functions for the calculator'''

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """adds whatever calcualtion has been made to history"""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """lists all the calculations from history"""
        return cls.history
    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()
