from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """adds whatever calcualtion has been made to history"""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """lists all the calculations from history"""
        return cls.history