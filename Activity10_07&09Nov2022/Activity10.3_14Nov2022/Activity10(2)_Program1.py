# Program to show Inheritance

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class B(A):
    def add(self):
        return self.x + self.y


obj2 = B(4, 5)
print("Sum =", obj2.add())