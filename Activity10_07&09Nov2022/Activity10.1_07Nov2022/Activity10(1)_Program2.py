# Define class and instance methods to calculate the volume of the cylinder

class Cylinder:
    pi = 3.14

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # instance method
    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    # class method
    @classmethod
    def description(cls):
        return f'This is class that computes volume of cylinder using Pi = {cls.pi}.'


if __name__ == "__main__":
    # create instance
    c1 = Cylinder(4, 2)

    # access instance method
    print("Volume of cylinder =", c1.volume())

    # access class method via class
    print(Cylinder.description())

    # access class method via instance
    print(c1.description())
