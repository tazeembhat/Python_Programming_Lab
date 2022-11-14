# Class and child class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def display(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


obj = Student("Tazeem", "Nazir")
obj.display()
