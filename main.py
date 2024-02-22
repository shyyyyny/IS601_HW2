"main.py"

import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class OperationCommand:
    """Represents a command to perform an operation."""
    def __init__(self, calculator, operation_name, arg_a, arg_b):
        """
        Initializes the OperationCommand.

        Args:
        - calculator: The calculator object.
        - operation_name: The name of the operation to perform.
        - a: The first operand.
        - b: The second operand.
        """
        self.calculator = calculator
        self.operation_name = operation_name
        self.arg_a = arg_a
        self.arg_b = arg_b

    def execute(self):
        """Executes the operation."""
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.arg_a, self.arg_b)
        raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(arg_a, arg_b, operation_name):
    """
    Calculates and prints the result of the operation.

    Args:
    - a: The first operand.
    - b: The second operand.
    - operation_name: The name of the operation.
    """
    try:
        a_decimal, b_decimal = map(Decimal, [arg_a, arg_b])
        command = OperationCommand(Calculator, operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {arg_a} {operation_name} {arg_b} is equal to {result}")
    except InvalidOperation:
        print("Invalid number input")
    except ZeroDivisionError:
        print("Error: Division by zero is not possible")
    except ValueError as e:
        print(e)

def main():
    """The main function."""
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()
