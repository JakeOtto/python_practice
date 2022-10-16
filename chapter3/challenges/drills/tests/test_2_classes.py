import sys

path = "./"

sys.path.append(path)

from lib._2_classes import *

class TestGreeter():

    def test_hello(self):
        self.subject = Greeter()
        assert self.subject.hello('Azrael') == 'Hello, Azrael' 

    def test_goodbye(self):
        self.subject = Greeter()
        assert self.subject.goodbye('Morticius') == 'Goodbye, Morticius'

    def test_goodnight(self):
        self.subject = Greeter()
        assert self.subject.goodnight('Jo') == 'Goodnight, Jo'
    
    def test_goodmorning(self):
        self.subject = Greeter()
        assert self.subject.goodmorning('Jo') == 'Goodmorning, Jo'

class TestCalculator():

    def test_add(self):
        self.subject = Calculator()
        assert self.subject.add(1,1) == 2

    def test_multiply(self):
        self.subject = Calculator()
        assert self.subject.multiply(2, 17) == 34

    def test_subract(self):
        self.subject = Calculator()
        assert self.subject.subtract(2, 17) == 15

    def test_divide(self):
        self.subject = Calculator()
        assert self.subject.divide(30, 3) == 10

class TestBasket():

    def test_add(self):
        self.subject = Basket()
        self.subject.add('eggs')
        self.subject.add('milk')
        self.subject.add('bread')
        assert self.subject.items == ['eggs', 'milk', 'bread']

class TestCohort():

    def test_add_student(self):
        self.subject = Cohort() 
        self.subject.add_student({'name' : 'Gene', 'employer' : 'Atlantis Digital'})
        self.subject.add_student({'name' : 'Petra', 'employer' : 'Atlantis Digital'})
        self.subject.add_student({'name' : 'Jaspal', 'employer' : 'Mercia Digital'})

        assert self.subject.students == ([
          {'name' : 'Gene', 'employer' : 'Atlantis Digital'},
          {'name' : 'Petra', 'employer' : 'Atlantis Digital'},
          {'name' : 'Jaspal', 'employer' : 'Mercia Digital'}
        ])

    def test_employed_by(self):
        self.subject = Cohort() 
        self.subject.add_student({'name' : 'Gene', 'employer' : 'Atlantis Digital'})
        self.subject.add_student({'name' : 'Petra', 'employer' : 'Atlantis Digital'})
        self.subject.add_student({'name' : 'Jaspal', 'employer' : 'Mercia Digital'})

        assert self.subject.employed_by('Atlantis Digital') == [
          {'name' : 'Gene', 'employer' : 'Atlantis Digital'},
          {'name' : 'Petra', 'employer' : 'Atlantis Digital'}
        ]

class TestPerson():

    def test_work_address(self):
        self.subject = Person({
          'name' : 'Jo',
          'pets' : [
            {'name' : 'Paulo', 'animal' : 'cat'},
            {'name' : 'Edith', 'animal' : 'dog'},
            {'name' : 'Pawel', 'animal' : 'goldfish'}
          ],
          'addresses' : [
            {'name' : 'work', 'building' : '12', 'street' : 'Whitehall'},
            {'name' : 'home', 'building' : '1', 'street' : 'North Lane'}
          ]
        })
        assert self.subject.work_address == '12 Whitehall'

    def test_home_address(self):
        self.subject = Person({
          'name' : 'Jo',
          'pets' : [
            {'name' : 'Paulo', 'animal' : 'cat'},
            {'name' : 'Edith', 'animal' : 'dog'},
            {'name' : 'Pawel', 'animal' : 'goldfish'}
          ],
          'addresses' : [
            {'name' : 'work', 'building' : '12', 'street' : 'Whitehall'},
            {'name' : 'home', 'building' : '1', 'street' : 'North Lane'}
          ]
        })
        assert self.subject.home_address == '1 North Lane'

    def test_pets(self):
        self.subject = Person({
          'name' : 'Jo',
          'pets' : [
            {'name' : 'Paulo', 'animal' : 'cat'},
            {'name' : 'Edith', 'animal' : 'dog'},
            {'name' : 'Pawel', 'animal' : 'goldfish'}
          ],
          'addresses' : [
            {'name' : 'work', 'building' : '12', 'street' : 'Whitehall'},
            {'name' : 'home', 'building' : '1', 'street' : 'North Lane'}
          ]
        })
        assert self.subject.pets == "Jo has 3 pets\n- a cat called Paulo\n- a dog called Edith\n- a goldfish called Pawel\n"