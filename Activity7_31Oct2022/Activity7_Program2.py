# Write a program to create a Simple Calculator using a switch case and function for every operation.

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def default():
    return "Invalid Operation!"

def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)


switcher = {1: add, 2: sub, 3: mul, 4: div, 5: mod}
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("1. Add\n"
      "2. Sub\n"
      "3. Multiply\n"
      "4. Division\n"
      "5. Modulo\n")
choice = int(input("Enter operation no.: "))
print("Ans =", switch(choice, x, y))

