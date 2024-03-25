#!/usr/bin/env python3
import datetime
class Person:
    """Class: representing Person"""
    raise_amount = 1.04 # This is the class variable
    number_of_employees = 0 # This is the class variable
    def __init__(self, surName, firstName, lastName, age, email=None, country=None, salary=5000):
        """The listed variables below are the instance variables"""
        self.surName = surName
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email or self.surName + self.firstName + self.lastName + "@gmail.com"
        self.country = country or "Nigeria"
        self.salary = salary
    
        Person.number_of_employees += 1
    def fullname(self):
        """Method: returning full name"""
        return self.surName + " " + self.firstName + " " + self.lastName
    def apply_raise(self):
        self.salary = int(self.salary * Person.raise_amount)
    @classmethod
    def change_raised_amount(cls, amount):
        cls.raise_amount = amount
    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True
    
class manager(Person):
    def __init__(self, surName, firstName, lastName, age, email=None, country=None, salary=5000, branch=None):
        super().__init__(surName, firstName, lastName, age, email, country, salary)
        self.branch = branch or "Ikotun Branch"

# This is "Instance" for class "Person"  
firstPerson = Person("Yusuf", "Shakiru", "Oluwasegun", 40)
print(f"Full Name: {firstPerson.fullname()}\nEmail:" 
      f"{firstPerson.email}\nAge: {firstPerson.age}\nCountry: {firstPerson.country}\nsalary: {firstPerson.salary}")

secondPerson = Person("Bolaji", "Isreal", "Babajide", 50, "isrealBabajide@gmail.com")
secondPerson.apply_raise()
print(secondPerson.__dict__.values())

thirdPerson = Person("Joseph", "Kate", "Parker", 30, "kate137@gmail.com", "New York")
Person.change_raised_amount(2.05)
thirdPerson.apply_raise()
print(thirdPerson.__dict__.values())

forthPerson = Person("Olatunji", "Badmus", "Remilekun", 35)
Person.raise_amount = 1.5
forthPerson.apply_raise()
print(forthPerson.__dict__.values())

my_date = datetime.date(1999, 2, 23)
print(Person.is_workday(my_date))
print(datetime.__all__)

Manager = manager("Ola", "Mide", "Sire", 60, "", "", "20000", "Ikoyi Branch")
print(Manager.__dict__.values())

print(isinstance(Manager, manager)) # check if Manager is an instance of manager
print(issubclass(manager, Person)) # check if manager is a subclass of Person

print(f"Current number of employees: {Person.number_of_employees}") 