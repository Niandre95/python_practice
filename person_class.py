# create by Andrew Bienvenue

#This is a simple person class

# creating a Person class
class Person(object):
    """This class print out the Person
    is name and age"""

# creating the constructor method
    def __init__(self, fname, lname, age):
        self.firstName = fname
        self.lastName = lname
        self.age = age

# creating a person object
person1 = Person("Andrew", "Bienvenue", 26)
person2 = Person("John", "Doe", 35)

#printing the person objects
print(f"Person 1 is {person1.firstName} {person1.lastName} and he is {person1.age} years old")
print(f"Person 2 is {person2.firstName} {person2.lastName} and he is {person2.age} years old")
