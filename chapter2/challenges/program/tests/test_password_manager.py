import sys

sys.path.append("./")

from lib import password_manager

class TestPasswordManager():

  def test_when_valid(self):
    self.subject_one = PasswordManager()
    self.subject_one.add('aceplay', '12345678!')
    assert self.subject_one.password_for('aceplay') == ('12345678!')
    assert self.subject_one.services == 'aceplay'
    self.subject_one.add("makerbnb", "12345678@")
    assert self.subject_one.services == ['aceplay', 'makerbnb']

  def test_when_invalid(self):
    self.subject_two = PasswordManager()
    self.subject_two.add('willslazerpalace', '1234567')
    self.subject_two.services == []
    self.subject_two.add('willslazerpalace', '12345678')
    self.subject_two.services == []

  def test_when_valid_characters(self):
    self.subject_two = PasswordManager()
    self.subject_two.add('willslazerpalace', '1234567!')
    self.subject_two.services == ['willslazerpalace']
    self.subject_two.add('discgolfuk', '1234567@')
    self.subject_two.services == ['willslazerpalace', 'discgolfuk']
    self.subject_two.add('deathmetalforcats', '1234567$')
    self.subject_two.add('snakesforsale', '1234567%')
    self.subject_two.add('whispergold', '1234567%')
    self.subject_two.services == ['willslazerpalace', 'discgolfuk', 'deathmetalforcats', 'snakesforsale', 'whispergold']
    