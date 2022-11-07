"""
Write a python program that accepts the length of three sides of a triangle
as inputs. The program should indicate whether the triangle is a
right-angled triangle. (Use Pythagorean theorem) Also find out its area
using Heron’s formula.
"""

import math


def right_triangle(a, b, c):
    if pow(c, 2) == pow(a, 2) + pow(b, 2):
        return True
    elif pow(a, 2) == pow(b, 2) + pow(c, 2):
        return True
    elif pow(b, 2) == pow(a, 2) + pow(c, 2):
        return True
    else:
        return False


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt((s * (s-a) * (s-b) * (s-c)))
    return area


s1 = int(input("Enter side of triangle: "))
s2 = int(input("Enter side of triangle: "))
s3 = int(input("Enter side of triangle: "))

if right_triangle(s1, s2, s3):
    print("It is a right angled triangle.")
else:
    print("It is not a right angled triangle.")

print("Area of given triangle = ", area_of_triangle(s1, s2, s3))
