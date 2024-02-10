import subprocess
import pytest

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input=input_data,
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],
    'division': [
        (['3', '5'], ['0', '0.6']),  # Example test case
        (['10', '2'], ['5', '5.0']),  # Additional test case
        (['8', '0'], ['Error'])       # Test case for division by zero
    ],
    'loops': [
        ('3\n', '0\n1\n4'),  # Example test case
        ('5\n', '0\n1\n4\n9\n16'),  # Additional test case
        ('0\n', ''),  # Test case for n=0
    ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', '\n'.join(input_data)) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', '\n'.join(input_data)) == '\n'.join(expected)

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', '\n'.join(input_data)) == '\n'.join(expected)

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data) == expected
