# Python3 program to show that we can create instance variables inside methods

class Dog:
    # Class Variable
    animal = 'dog'

    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def set_color(self, color):
        self.color = color

    # Retrieves instance variable
    def get_color(self):
        return self.color


# Driver Code
Rodger = Dog("Pug")
Rodger.set_color("Brown")
print("Breed:", Rodger.breed)
print("Color:", Rodger.get_color())