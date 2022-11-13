"""
Python program to show that the variables with a value assigned in the class declaration,
are class variables and variables inside methods and constructors are instance variables.
"""


class Dog:
    # Class Variable
    animal = 'dog'

    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

# Class variables can be accessed using class name also
print("Accessing class variable using class name:")
print(Dog.animal)
