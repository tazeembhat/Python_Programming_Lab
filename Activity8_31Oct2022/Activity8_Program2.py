# Create a function that takes three numbers as arguments and returns the largest of them

def maxof3(a, b, c):
    list = [a, b, c]
    return max(list)


def maximum(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c

    return largest


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

print("Max of [x, y, z]: ", maxof3(x, y, z))
print("Max of [x, y, z]: ", maximum(x, y, z))
# max() is in-built function in python
print("Max of [x, y, z]: ", max(x, y, z))
