class Person:
    """Class: representing Person"""
    raise_amount = 1.04  # Class variable
    number_of_employees = 0  # Class variable

    def __init__(self, surName, firstName, lastName, age, email=None, country=None, salary=5000):
        """Instance variables initialization"""
        self.surName = surName
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email or surName + firstName + lastName + "@gmail.com"
        self.country = country or "Nigeria"
        self.salary = salary
        Person.number_of_employees += 1

    def fullname(self):
        """Returning full name"""
        return f"{self.surName} {self.firstName} {self.lastName}"

    def apply_raise(self):
        """Applying raise to salary"""
        self.salary = int(self.salary * Person.raise_amount)

# Instance creation and usage
firstPerson = Person("Yusuf", "Shakiru", "Oluwasegun", 40)
print(f"Full Name: {firstPerson.fullname()}\nEmail: {firstPerson.email}\nAge: {firstPerson.age}\nCountry: {firstPerson.country}\nSalary: {firstPerson.salary}")

secondPerson = Person("Bolaji", "Isreal", "Babajide", 50, "isrealBabajide@gmail.com")
secondPerson.apply_raise()
print(secondPerson.__dict__)

thirdPerson = Person("Joseph", "Kate", "Parker", 50, "kate137@gmail.com", "New York")
Person.raise_amount = 2.05
thirdPerson.apply_raise()
print(thirdPerson.__dict__)

print(f"Current number of employees: {Person.number_of_employees}")
