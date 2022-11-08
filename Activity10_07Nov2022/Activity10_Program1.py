# define a class that can add and subtract two numbers.

class AddSub:
    # Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Method to add two numbers
    def add(self):
        return self.num1 + self.num2

    # Method to sub two numbers
    def sub(self):
        return self.num1 - self.num2


if __name__ == '__main__':
    x = 10
    y = 5
    # Create object of class
    obj = AddSub(x, y)

    print(f'{x} + {y} = {obj.add()}')
    print(f'{x} - {y} = {obj.sub()}')
