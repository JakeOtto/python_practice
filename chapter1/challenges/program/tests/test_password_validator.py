import sys

path = "./"

sys.path.append(path)

from lib.password_validator import valid

def test_whether_the_program_validates():
  assert valid("1234567") == False, "returns false when the password is less than 8 chars"
  assert valid("123456789") == False, "returns false when the password is less than 8 chars"
  
  assert valid("567!") == False, "returns false when the password contains less than eight characters but includes '!'"
  assert valid("567@") == False, "returns false when the password contains less than eight characters but includes '@'"
  assert valid("567$") == False, "returns false when the password contains less than eight characters but includes '$'"
  assert valid("567&") == False, "returns false when the password contains less than eight characters but includes '&'"
  assert valid("567%") == False, "returns false when the password contains less than eight characters but includes '%'"

  assert valid("12345678") == False, "returns false when the password does not contain any special characters"

  assert valid("1234567!") == True
  assert valid("1234567@") == True
  assert valid("1234567$") == True
  assert valid("1234567%") == True
  assert valid("1234567&") == True