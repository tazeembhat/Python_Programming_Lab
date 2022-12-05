# Hierarchical Inheritance

class Parent:
    def func1(self):
        print("This is function 1")


class Child(Parent):
    def func2(self):
        print("This is function 2")


class Child2(Parent):
    def func3(self):
        print("This is function 3")


obj = Child()
obj1 = Child2()
obj.func1()
obj.func2()
obj1.func3()
