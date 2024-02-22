"conftest.py"

from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data for parameterized tests.

    Args:
    - num_records: Number of test records to generate.

    Yields:
    - Tuple: A tuple containing operands, operation name, operation function, and expected result.
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for _ in range(num_records):
        arg_a = Decimal(fake.random_number(digits=2))
        arg_b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operations.keys()))
        operation_func = operations[operation_name]
        if operation_func == divide():  # Add parentheses to call the function
            arg_b = Decimal('1') if arg_b == Decimal('0') else arg_b
        expected = "ZeroDivisionError" if operation_func == divide() and arg_b == Decimal('0') else operation_func(arg_a, arg_b)
        yield arg_a, arg_b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Add custom command-line option for specifying the number of test records to generate.

    Args:
    - parser: The pytest command-line parser.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate tests based on the provided test data.

    Args:
    - metafunc: Metafunc object representing the test function.
    """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
