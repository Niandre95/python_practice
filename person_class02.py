# create by Andrew Bienvenue

#This is a simple person class with a method

# creating a Person class
class Person(object):
    """This class print out the Person
    is name and age"""

# creating the constructor method
    def __init__(self, fname, lname, age):
        self.firstName = fname
        self.lastName = lname
        self.age = age

    def __str__(self):
        return (f"first name : {self.firstName} , last name : {self.lastName} and age:{self.age}")

    def introduction(self):
        print(f"Hi, my name is {self.firstName} {self.lastName} and I am {self.age} years old")

# creating a person object
person1 = Person("Andrew", "Bienvenue", 26)
person2 = Person("John", "Doe", 35)

# printing the objects
print("The class object Information:")
print(person1)
print(person2)
# calling the method to print the person objects
print("\nIntroducing the class object:")
person1.introduction()
person2.introduction()
