
import sys

path = "./"

sys.path.append(path)

from lib._1_lists_and_dictionaries import *

class TestArraysOne():

    def test_fourth_element():
        assert fourth_element([1, 2, 3, 4, 5]) == 4

    def test_average():
        assert average([1, 2, 3, 4, 5]) == 3

    def test_lowest_squared():
        assert lowest_squared([2, 3, 4, 5]) == 4

    def test_highest_squared():
        assert highest_squared([2, 3, 4, 5]) == 25


class TestDictionariesOne():

    def test_values_summed():
        assert values_summed({'one': 1, 'two': 2, 'three': 3}) == 6

    def test_first_two_keys():
        assert first_two_keys({'one': 1, 'two': 2, 'three': 3}) == [
            'one', 'two']

    def test_first_two_values():
        assert first_two_values({'one': 1, 'two': 2, 'three': 3}) == [1, 2]


class TestArraysTwo():

    def test_starts_with_a():
        assert starts_with_a(
            ['aardvark', 'apple', 'zebra', 'zinc']) == ['aardvark', 'apple']

    def test_starts_with_a_vowel():
        assert starts_with_a_vowel(
            ['apple', 'pear', 'orange', 'egg', 'indigo', 'uncle']) == ['apple', 'orange', 'egg', 'indigo', 'uncle']

    def test_reverse_each_element():
        assert reverse_each_element(
            ['one', 'two']) == ['eno', 'owt']

    def test_sort_by_last_letter():
        assert sort_by_last_letter(
            ['apple', 'pear', 'satsuma']) == ['satsuma', 'apple', 'pear']

    def test_greater_than_5():
        assert greater_than_5(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [6, 7, 8, 9, 10]

    def test_greater_than_x():
        assert greater_than(
            [1, 2, 3, 4, 5], 3) == [4, 5]

    def test_less_than():
        assert less_than([1, 2, 3, 4, 5], 3) == [1, 2]

    def test_words_shorter_than():
        assert words_shorter_than(
            ['tree', 'rainbow', 'desk', 'computer'], 5) == ['tree', 'desk']

    def test_all_above():
        assert all_above([2, 3, 4, 5], 1) == True
        assert all_above([2, 3, 4, 5], 5) == False

    def test_all_below():
        assert all_below([2, 3, 4, 5], 6) == True
        assert all_below([2, 3, 4, 5], 5) == False

    def test_multiply_by_each():
        assert multiply_each_by(
            [1, 2, 3, 4, 5], 2) == [2, 4, 6, 8, 10]


class TestDictionariesTwo():

    def test_where_value_below():
        assert where_value_below(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 5
        ) == (
            {'chips': 2.5, 'slaw': 2.0, 'salad': 3.0}
        )

    def test_where_key_starts_with():
        assert where_key_starts_with(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 's'
        ) == (
            {'slaw': 2.0, 'salad': 3.0}
        )

    def test_add_key_value_pair():
        assert add_key_value_pair(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 'beans', 2.0
        ) == (
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0, 'beans': 2.0}
        )

    def test_sort_by_key():
        assert sort_by_key(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0, 'beans': 2.0}
        ) == (
            {"beans": 2.0, "burger": 10, "chips": 2.5, "salad": 3.0, "slaw": 2.0}
        )

    def test_sort_by_value():
        assert sort_by_value(
            {'drummer': 'ringo', 'guitar': 'jimmy', 'vocals': 'nina'}
        ) == (
            {"guitar": "jimmy", "vocals": "nina", "drummer": "ringo"}
        )
