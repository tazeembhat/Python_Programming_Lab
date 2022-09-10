# Python Program to calculate th length of string without using len().

str1 = input("Enter the string: ")

count = 0
for i in str1:
    count = count+1

print("Length of String is", count)
