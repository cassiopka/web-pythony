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
    ],
    'print_function': [
        ('5\n', '12345'),  # Example test case
        ('10\n', '12345678910'),  # Additional test case
        ('1\n', '1'),  # Test case for n=1
        ('20\n', '1234567891011121314151617181920'),  # Test case for n=20
        ('0\n', 'Error'),  # Test case for n=0
        ('21\n', 'Error')  # Test case for n=21
    ],
    # 'second_score': [
    #     ('5\nГарри\n37.21\nБерри\n37.21\nТина\n37.2\nАкрити\n41\nХарш\n39\n', 'Берри\nГарри'),  # Example test case
    # ],
    'lists': [
        ('12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n', '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]'),  # Example test case
        ('6\ninsert 0 1\ninsert 1 2\ninsert 2 3\nprint\nreverse\nprint\n', '[1, 2, 3]\n[3, 2, 1]'),  # Additional test case
        ('5\nappend 5\ninsert 0 4\ninsert 1 2\ninsert 2 3\nprint\n', '[4, 2, 3, 5]')    ],
    'swap_case': [
        ('Www.MosPolytech.ru\n', 'wWW.mOSpOLYTECH.RU'),  # Example test case
        ('Pythonist 2\n', 'pYTHONIST 2'),  # Additional test case
        ('aBcDeF\n', 'AbCdEf'),  # Test case with both lower and upper case letters
        ('1234\n', '1234'),  # Test case with only digits
        ('!@#$\n', '!@#$'),  # Test case with special characters
    ],
    'split_and_join': [
        ('this is a string\n', 'this-is-a-string'),  # Example test case
        ('Hello World\n', 'Hello-World'),  # Additional test case
        ('1 2 3 4 5\n', '1-2-3-4-5'),  # Test case with digits
        ('!@#$ %^&*\n', '!@#$-%^&*'),  # Test case with special characters and whitespace
        (' \n', '')  # Test case with only whitespace
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

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data) == expected

# @pytest.mark.parametrize("input_data, expected", test_data['second_score'])
# def test_second_score(input_data, expected):
#     assert run_script('second_score.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data) == expected

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input=input_data,
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

def test_max_word():
    expected_output = "сосредоточенности"
    assert run_script('max_word.py') == expected_output
