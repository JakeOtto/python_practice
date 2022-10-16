import sys

sys.path.append("./")

from lib._2_classes import *

class TestInstances():
  def test_animal():
    new_animal = Animal()
    assert isinstance(new_animal, Animal)

  def test_vehicle():
    vw_golf = Vehicle()
    assert isinstance(vw_golf, Vehicle)

class TestAnimalsSpeak():
  def test_cat():
    azrael = Cat()
    assert azrael.speak() == 'miaow'

  def test_dog():
    white_fang = Dog()
    assert white_fang.speak() == 'woof'

class TestStringFormatter():

  def test_block_caps(self):
    self.subject = StringFormatter()
    assert self.subject.block_caps('hello') == "HELLO"

  def test_lower_case(self):
    self.subject = StringFormatter()
    assert self.subject.lower_case('HELLO') == 'hello'

class TestCalculator():

  def test_add(self):
    self.subject = Calculator()
    assert self.subject.add(2, 2) == 4
  
  def test_multiply(self):
    self.subject = Calculator()
    assert self.subject.multiply(2, 17) == 34

  def test_subract(self):
    self.subject = Calculator()
    assert self.subject.subtract(2, 17) == 15

  def test_divide(self):
    self.subject = Calculator()
    assert self.subject.divide(30, 3) == 10

class TestApprentice():

  def test_name(self):
    self.subject = Apprentice('Jude', 'August 2045')
    assert self.subject.name == 'Jude'

  def test_cohort(self):
    self.subject = Apprentice('Jude', 'August 2045')
    assert self.subject.cohort == 'August 2045'

  def test_full_details(self):
    self.subject = Apprentice('Jude', 'August 2045')
    assert self.subject.full_details() == 'Jude, August 2045'
  

class TestCohort():

  def test_name(self):
    self.subject = Cohort('January 2060', '2060/01/01', '2060/01/08')
    assert self.subject.name == "January 2060"

  def test_start_date(self):
    self.subject = Cohort('January 2060', '2060/01/01', '2060/01/08')
    assert self.subject.start_date == '2060/01/01'

  def test_end_date(self):
    self.subject = Cohort('January 2060', '2060/01/01', '2060/01/08')
    assert self.subject.end_date == '2060/01/08'

  def test_duration(self):
    self.subject = Cohort('January 2060', '2060/01/01', '2060/01/08')
    assert self.subject.duration == 7