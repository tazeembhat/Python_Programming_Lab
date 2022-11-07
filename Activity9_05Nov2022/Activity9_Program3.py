# Reverse words in a given String in Python

def reverse_string(s):
    list1 = s.split()
    s = list1[::-1]
    rev = " "
    return rev.join(s)


str1 = input("Enter the string: ")
print("Original String:", str1)
print("Reversed String:", reverse_string(str1))
