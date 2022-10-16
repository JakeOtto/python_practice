import sys

path = "./"

sys.path.append(path)

from lib._1_lists_and_dictionaries import *

def test_first_element():
  assert first_element([1, 2, 3]) == 1

def test_second_element():
  assert second_element([1, 2, 3]) == 2

def test_last_element():
  assert last_element([1, 2, 3]) == 3

def test_first_two_element():
  assert first_two_element([1, 2, 3]) == [1, 2]

def test_first_three_element():
  assert first_three_element([1, 2, 3]) == [1, 2, 3]

def test_total():
  assert total([1, 2, 3, 4]) == 10

def test_lowest_number():
  assert lowest_number([2,5,3,1,4]) == 1

def test_highest_number():
  assert highest_number([2,5,3,1,4]) == 5

def test_the_beatles():
  assert the_beatles() == ['john', 'paul', 'george', 'ringo']

def test_i_joined_the_beatles():
  assert i_joined_the_beatles("Xavier") == ['john', 'paul', 'george', 'ringo', 'Xavier']

def test_we_joined_the_beatles():
  assert we_joined_the_beatles("Iggy", "Sandra") == ['john', 'paul', 'george', 'ringo', 'Iggy', 'Sandra']

def test_remove_nones_from_array():
  assert remove_nones_from_array([None, 3, 2, 6, None, 7]) == [3, 2, 6, 7] 

def test_double_array():
  assert double_array([1,2,3]) == [1, 2, 3, 1, 2, 3]

def test_unique_elements():
  assert unique_elements([1, 1, 2, 2, 3, 3]) == [1,2,3]

def add_to_array():
  assert add_to_array(['one', 'two', 'three'], 'four') == ['one', 'two', 'three', 'four']

def test_new_band_member():
  assert new_band_member({'drummer' : 'kermit'}) == {'vocalist' : 'miss piggy', 'lead_guitar' : 'scooter', 'drummer' : 'kermit'}

def test_all_values():
  assert all_values({'one' : 1, 'two' : 2, 'three' : 3}) == [1,2,3]

def test_all_keys():
  assert all_keys({'one' : 1, 'two' : 2, 'three' : 3}) == ['one', 'two', 'three']

def test_remove_nones_from_dictionary():
  assert remove_nones_from_dictionary({'one' : None, 'two' : 2, 'three' : 3}) == ({'two' : 2, 'three' : 3})

def test_key_value_swap():
  assert key_value_swap({'one' : 1, 'two' : 2, 'three' : 3}) == ({1 : 'one', 2 : 'two', 3 : 'three'})

def test_touch_in():
  assert touch_in('Aldgate East', '2022/01/30 11:12') == ({'entrypoint' : 'Aldgate East', 'time' : '2022/01/30 11:12'})

