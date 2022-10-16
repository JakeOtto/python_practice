
import sys

path = "./"

sys.path.append(path)

from lib._1_calling_methods import *

def test_caps_a_string():
    assert block_caps_a_string("hello") == "HELLO"

def test_lower_case_a_string():
    assert lower_case_a_string('HELLO WORLD') == 'hello world'

def test_length_of_string():
    assert length_of_a_string('the length of this string is 31') == 31

def test_reverse_a_string():
    assert reverse_a_string("sdrawkcab") == 'backwards'

def test_swap_case_string():
    assert swap_the_case_of_a_string('Hello World') == 'hELLO wORLD'

def test_is_integer_odd():
    assert is_integer_odd(1) == True
    assert is_integer_odd(2) == False, "Integer is not odd"

def test_is_integer_even():
    assert is_integer_even(2) == True
    assert is_integer_even(7) == False, "Integer is not even"


def test_integer_to_float():
    assert integer_to_float(17) == 17.0
    assert integer_to_float(1234) == 1234.0

def test_return_previous_integer():
    assert return_previous_integer(3) == 2
    assert return_previous_integer(8) == 7

def test_return_next_integer():
    assert return_next_integer(4) == 5
    assert return_next_integer(189) == 190

def test_round_up():
    assert round_up(17.7) == 18
    assert round_up(34567.112) == 34568.0

def test_round_down():
    assert round_down(18.8) == 18
    assert round_down(999.99) == 999.0

def test_float_to_string():
    assert float_to_string(656.6) == "656.6"

def test_float_to_integer():
    assert float_to_integer(18.8) == 18

def test_float_is_positive():
    assert float_is_positive(1.1) == True
    assert float_is_positive(-567.2) == False

def test_float_is_negetive():
    assert float_is_negative(-1.1) == True
    assert float_is_negative(98765) == False

def test_boolean_to_string():
    assert boolean_to_string(True) == "True"
    assert boolean_to_string(False) == "False"
    

