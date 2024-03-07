import pytest
from fact import fact_rec, fact_it

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (5, 120),
    (10, 3628800),
    (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000),
])
def test_fact_rec(n, expected):
    if n <= 500:  
        assert fact_rec(n) == expected
    else:
        pytest.skip("Рекурсивная функция не поддерживает столь большие значения n")

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (5, 120),
    (10, 3628800),
    (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000),
])
def test_fact_it(n, expected):
    assert fact_it(n) == expected

from show_employee import show_employee

@pytest.mark.parametrize("name, salary, expected_output", [
    ("Alice", 100000, "Alice: 100000 ₽"),
    ("Bob", 150000, "Bob: 150000 ₽"),
    ("Eve", 80000, "Eve: 80000 ₽")
])
def test_show_employee(name, salary, expected_output):
    assert show_employee(name, salary) == expected_output

def test_show_employee_default_salary():
    assert show_employee("Sam") == "Sam: 100000 ₽"

def test_show_employee_custom_salary():
    assert show_employee("Emma", 110000) == "Emma: 110000 ₽"

def test_show_employee_no_name():
    with pytest.raises(TypeError):
        show_employee()


def test_show_employee_with_salary():
    name = "Иванов Иван Иванович"
    salary = 30000
    expected = "Иванов Иван Иванович: 30000 ₽"
    assert show_employee(name, salary) == expected

def test_show_employee_without_salary():
    name = "Петров Петр Петрович"
    expected = "Петров Петр Петрович: 100000 ₽"
    assert show_employee(name) == expected


from sum_and_sub import sum_and_sub

@pytest.mark.parametrize("a, b, expected_sum, expected_sub", [
    (3, 5, 8, -2),
    (-2.5, 7.3, 4.8, -9.8),
    (0, 0, 0, 0),
    (10, -4, 6, 14),
])
def test_sum_and_sub(a, b, expected_sum, expected_sub):
    sum_, sub_ = sum_and_sub(a, b)
    assert sum_ == expected_sum
    assert sub_ == expected_sub


from process_list import process_list_lc, process_list_gen

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3, 4, 5], [1, 4, 9, 8, 25]),
    ([10, -3, 6, 0, -7], [20, 9, 12, 0, 49]),
    ([], []),
])
def test_process_list(arr, expected):
    assert process_list_lc(arr) == expected
    assert list(process_list_gen(arr)) == expected
    

@pytest.fixture
def sample_input():
    return [1, 2, 3, 4, 5]

def test_process_list_lc(sample_input):
    expected_output = [1, 4, 9, 8, 25]
    output = process_list_lc(sample_input)
    assert output == expected_output

def test_process_list_gen(sample_input):
    expected_output = [1, 4, 9, 8, 25]
    output = list(process_list_gen(sample_input))
    assert output == expected_output



from my_sum import my_sum

def test_my_sum():
    assert my_sum() == 0

@pytest.mark.parametrize("args, expected", [
    ((1, 2, 3), 6),
    ((-2.5, 7.3, 0, 10), 14.8),
    ((0.1, 0.2, 0.3, 0.4, 0.5), 1.5),
])
def test_my_sum_args(args, expected):
    assert my_sum(*args) == expected

def test_my_sum_with_empty_args():
    assert my_sum() == 0

def test_my_sum_with_single_arg():
    assert my_sum(5) == 5

def test_my_sum_with_multiple_args():
    assert my_sum(1, 2, 3, 4) == 10

def test_my_sum_with_negative_args():
    assert my_sum(-1, -2, -3) == -6


import subprocess
import sys

def run_my_sum_argv(*args):
    cmd = [sys.executable, "my_sum_argv.py"] + list(map(str, args))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def test_my_sum_argv():
    args = []
    assert run_my_sum_argv(*args) == "0"

@pytest.mark.parametrize("args, expected", [
    ((1, 2, 3), "6.0"),
    ((-2.5, 7.3, 0, 10), "14.8"),
    ((0.1, 0.2, 0.3, 0.4, 0.5), "1.5"),
])
def test_my_sum_argv_args(args, expected):
    assert run_my_sum_argv(*args) == expected
    
    
import os
import tempfile

from files_sort import sort_files_by_extension

def create_test_files(directory, filenames):
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as f:
            pass

def test_files_sort():
    with tempfile.TemporaryDirectory() as temp_dir:
        filenames = ["a.py", "a.txt", "b.py", "b.txt", "c.py", "c.txt"]
        create_test_files(temp_dir, filenames)

        sorted_files = sort_files_by_extension(temp_dir)
        expected_sorted_files = ["a.py", "b.py", "c.py", "a.txt", "b.txt", "c.txt"]
        assert sorted_files == expected_sorted_files


import os
import tempfile
import shutil
import sys
from contextlib import redirect_stdout

from file_search import find_file

def create_test_files(directory, filenames, content=None):
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            if content:
                f.write("\n".join(content))

def test_find_file(capfd):
    with tempfile.TemporaryDirectory() as temp_dir:
        search_file = "test.txt"
        other_files = ["file1.txt", "file2.txt"]
        content = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]

        create_test_files(temp_dir, [search_file] + other_files, content)

        # Создаем поддиректорию и копируем искомый файл
        subdir = os.path.join(temp_dir, "subdir")
        os.mkdir(subdir)
        shutil.copy(os.path.join(temp_dir, search_file), subdir)

        with redirect_stdout(sys.stdout):
            result = find_file(search_file, temp_dir)

        output = capfd.readouterr().out.strip().replace('\n\n', '\n')
        expected_output = "\n".join(content[:5])

        assert result is True
        assert output == expected_output

from fibonacci import fibonacci, cube

def test_cube():
    assert cube(0) == 0
    assert cube(1) == 1
    assert cube(2) == 8
    assert cube(3) == 27

def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_cube():
    assert list(map(cube, fibonacci(1))) == [0]
    assert list(map(cube, fibonacci(2))) == [0, 1]
    assert list(map(cube, fibonacci(5))) == [0, 1, 1, 8, 27]
    assert list(map(cube, fibonacci(10))) == [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]

from average_scores import compute_average_scores

def test_compute_average_scores():
    scores = (
        (89, 90, 78, 93, 80),
        (90, 91, 85, 88, 86),
        (91, 92, 83, 89, 90.5)
    )
    expected_average_scores = (90.0, 91.0, 82.0, 90.0, 85.5)
    assert compute_average_scores(scores) == expected_average_scores

def test_compute_average_scores_one_student():
    scores = ((100,),)
    expected_average_scores = (100.0,)
    assert compute_average_scores(scores) == expected_average_scores

def test_compute_average_scores_one_subject():
    scores = (
        (89, 90, 78, 93, 80),
    )
    expected_average_scores = (89.0, 90.0, 78.0, 93.0, 80.0)
    assert compute_average_scores(scores) == expected_average_scores


from plane_angle import Point, plane_angle


def test_plane_angle():
    a = Point(1, 0, 0)
    b = Point(0, 1, 0)
    c = Point(0, 0, 1)
    d = Point(1, 1, 1)
    expected_angle = pytest.approx(70.52877936550931, abs=1e-06)
    assert plane_angle(a, b, c, d) == expected_angle

def test_plane_angle_parallel():
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(0, 1, 0)
    d = Point(1, 1, 0)
    expected_angle = 180.0
    assert plane_angle(a, b, c, d) == expected_angle

from phone_number import sort_phone

def test_sort_phone():
    input_phones = [
        "07895462130",
        "89875641230",
        "9195969878"
    ]
    expected_output = [
        "+7 (789) 546-21-30",
        "+7 (919) 596-98-78",
        "+7 (987) 564-12-30"
    ]
    assert sort_phone(input_phones) == expected_output

def test_sort_phone_with_plus():
    input_phones = [
        "+78954621300",
        "+79875641230",
        "+79195969878"
    ]
    expected_output = [
        "+7 (895) 462-13-00",
        "+7 (919) 596-98-78",
        "+7 (987) 564-12-30"
    ]
    assert sort_phone(input_phones) == expected_output

from complex_numbers import Complex

def test_addition():
    x = Complex(2, 1)
    y = Complex(5, 6)
    result = x.add(y)
    assert str(result) == "7.00+7.00i"

def test_subtraction():
    x = Complex(2, 1)
    y = Complex(5, 6)
    result = x.sub(y)
    assert str(result) == "-3.00-5.00i"

def test_multiplication():
    x = Complex(2, 1)
    y = Complex(5, 6)
    result = x.mul(y)
    assert str(result) == "4.00+17.00i"

def test_division():
    x = Complex(2, 1)
    y = Complex(5, 6)
    result = x.truediv(y)
    assert str(result) == "0.26-0.11i"

def test_modulus():
    x = Complex(2, 1)
    y = Complex(5, 6)
    result_x = x.mod()
    result_y = y.mod()
    assert str(result_x) == "2.24+0.00i"
    assert str(result_y) == "7.81+0.00i"
    
    
from log_decorator import function_logger
import os

@pytest.fixture
def log_file(tmpdir):
    file_path = tmpdir.join("test.log")
    return str(file_path)

def test_function_logger(log_file):
    @function_logger(log_file)
    def add(a, b):
        return a + b

    add(1, 2)

    with open(log_file, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 7
        assert 'add\n' in lines[0]
        assert '(1, 2)\n' in lines[2]
        assert '3\n' in lines[3]

    os.remove(log_file)
    
    
    
from people_sort import sort_people_by_age

def test_sort_people_by_age():
    people = [["Mike", "Thomson", "20", "M"],
              ["Robert", "Bustle", "32", "M"],
              ["Andria", "Bustle", "30", "F"]]
    sorted_people = sort_people_by_age(people)
    assert sorted_people == [["Mike", "Thomson", "20", "M"],
                             ["Andria", "Bustle", "30", "F"],
                             ["Robert", "Bustle", "32", "M"]]



from email_validation import is_valid_email, filter_valid_emails

def test_is_valid_email():
    assert is_valid_email("lara@mospolytech.ru") == True
    assert is_valid_email("brian-23@mospolytech.ru") == True
    assert is_valid_email("britts_54@mospolytech.ru") == True
    assert is_valid_email("invalid_email") == False
    assert is_valid_email("invalid.com") == False

def test_filter_valid_emails():
    emails = ["lara@mospolytech.ru", "brian-23@mospolytech.ru", "britts_54@mospolytech.ru", "invalid_email"]
    valid_emails = filter_valid_emails(len(emails), emails)
    assert valid_emails == ["brian-23@mospolytech.ru", "britts_54@mospolytech.ru", "lara@mospolytech.ru"]


from circle_square_mk import circle_square_mk

def test_circle_square_mk():
    radius = 5
    n_experiments = 100000
    calculated_square = circle_square_mk(radius, n_experiments)
    actual_square = 3.14159 * radius ** 2  
    error = abs(calculated_square - actual_square)

    assert error < 1  

