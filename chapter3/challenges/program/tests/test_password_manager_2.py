import sys

path = "./"

sys.path.append(path)

from lib.password_manager_2 import *

class TestPasswordManager2():

	def test_add_and_services(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		self.password_manager.add('makersbnb', 'qwerty789')
		assert self.password_manager.services ==  ['acebook', 'makersbnb'], 'added when the password and service name are unique'

	def test_not_adding(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		self.password_manager.add('makersbnb', 'password123')
		assert self.password_manager.services ==  ['acebook'], 'not added when the password is not unique'

	def test_not_adding_not_unique(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		self.password_manager.add('acebook', 'qwerty789')
		assert self.password_manager.services ==  ['acebook'], 'not added when the service name is not unique'

	def test_delete(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')		
		self.password_manager.remove('acebook')
		assert self.password_manager.services ==  [], "removes a service"

	def test_update(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		self.password_manager.add('makersbnb', 'qwerty789')
		self.password_manager.update('acebook', 'newpassword456')
		assert self.password_manager.password_for('acebook') ==  'newpassword456', 'updates when password is unique'

	def test_update_not_unique(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('willslazeremporium', 'password123')
		self.password_manager.add('metalfistrecords', 'qwerty789')
		self.password_manager.update('willslazeremporium', 'qwerty789')
		assert self.password_manager.password_for('willslazeremporium') ==  'password123', 'does not update when password is not unique' 

	def test_sort_by_alphabetically(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		self.password_manager.add('makersbnb', 'qwerty789')
		assert self.password_manager.sort_by('service') ==  [
        'acebook',
        'makersbnb'
      ]

	def test_sort_reverse_alphabetically(self):
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		self.password_manager.add('makersbnb', 'qwerty789')
		assert self.password_manager.sort_by('service', 'reverse') ==  [
        'makersbnb',
        'acebook'
      ]

	def test_sort_chronologically(self):
		import time
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		time.sleep(2)
		self.password_manager.add('makersbnb', 'qwerty789')
      
		assert self.password_manager.sort_by('added_on') ==  [
        'makersbnb',
        'acebook'
      ]

	def test_sort_reverse_chronologically(self):
		import time
		self.password_manager = PasswordManager2()
		self.password_manager.add('acebook', 'password123')
		time.sleep(2)
		self.password_manager.add('makersbnb', 'qwerty789')
      
		assert self.password_manager.sort_by('added_on', 'reverse') == [
        'makersbnb',
        'acebook'
      ]