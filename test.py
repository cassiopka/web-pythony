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
        (['3', '5'], ['0', '0.6']),  
        (['10', '2'], ['5', '5.0']),  
        (['8', '0'], ['Error'])       
    ],
    'loops': [
        ('3\n', '0\n1\n4'),  
        ('5\n', '0\n1\n4\n9\n16'),  
    ],
    'print_function': [
        ('5\n', '12345'),  
        ('10\n', '12345678910'),  
        ('1\n', '1'),  
        ('20\n', '1234567891011121314151617181920'),  
        ('0\n', 'Error'),  
        ('21\n', 'Error')  
    ],
    'nested_list': [
        ('5\nГарри\n37.21\nБерри\n37.21\nТина\n37.2\nАкрити\n41\nХарш\n39\n', 'Гарри\nБерри'),  # Example test case
    ],
    'lists': [
        ('12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n', '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]'),  # Example test case
        ('6\ninsert 0 1\ninsert 1 2\ninsert 2 3\nprint\nreverse\nprint\n', '[1, 2, 3]\n[3, 2, 1]'),  # Additional test case
        ('5\nappend 5\ninsert 0 4\ninsert 1 2\ninsert 2 3\nprint\n', '[4, 2, 3, 5]')    ],
    'swap_case': [
        ('Www.MosPolytech.ru\n', 'wWW.mOSpOLYTECH.RU'),  
        ('Pythonist 2\n', 'pYTHONIST 2'), 
        ('aBcDeF\n', 'AbCdEf'), 
        ('1234\n', '1234'), 
        ('!@#$\n', '!@#$'), 
    ],
    'split_and_join': [
        ('this is a string\n', 'this-is-a-string'),  
        ('Hello World\n', 'Hello-World'),  
        ('1 2 3 4 5\n', '1-2-3-4-5'),  
        ('!@#$ %^&*\n', '!@#$-%^&*'),  
        (' \n', '')  
    ],
    'are_anagrams': [
        ('listen\nsilent\n', 'YES'),
        ('triangle\nintegral\n', 'YES' ),
        ('cat\ntac1\n', 'NO'),
        ('hello world\nworld hello\n' , 'YES'),
        ('Listen\nsilent\n', 'NO')
    ],
    'metro': [
        (('1\n0 3\n3'), '0'),  
    ], 
    'minion_game': [
        (('BANANA\n'),'Стюарт 12'),
        (('AEIOU\n'), 'Кевин 15'),
        (('BCDFG\n'), 'Стюарт 15')
    ],
    'is_leap': [
        ('2016\n', 'True'),
        ('2024\n', 'True'),
        ('2000\n', 'True'),
        ('2400\n', 'True'),
        ('2017\n', 'False'),
        ('1900\n', 'False'),
        ('2100\n', 'False'),
        ('2200\n', 'False')
    ],
        'happiness': [
        (('3 2\n 1 5 3\n 3 1\n 5 7\n'), '1'),
        (('4 3\n 10 15 20 25\n 15 10 5\n 20 25 30\n'), '0'),
        (('5 3\n 100 200 300 400 500\n 200 300 400\n 100 150 250\n'),'2'),
        (('2 5\n 1 1\n 1 2 3 4 5\n 6 7 8 9 10\n'), '2'),
        (('5 5\n 10 20 30 40 50\n 30 40\n 10 20\n'), '0')
    ],
        'pirate': [
        ('10 3\n bananas 8 20\n apples 5 15\nwatermelons 12 30', 'apples 5 15\nbananas 5 12.5')
    ],
        'matrix':
    [
        ('2\n 1 2\n 3 4\n 1 0\n 0 1\n', '1 2\n3 4')
    ],
    'second_score':[
        ('5\n2 3 6 6 5\n', '5')
    ]
        
}

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

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['are_anagrams'])
def test_are_anagramg(input_data, expected):
    assert run_script('anagram.py', input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate'])
def test_pirate(input_data, expected):
    assert run_script('pirate_ship.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix'])
def test_matrix(input_data, expected):
    assert run_script('matrix_mult.py', input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data) == expected


def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

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

def test_price_sum():
    expected_output = "6842.84 5891.06 6810.90"
    assert run_script('price_sum.py') == expected_output
