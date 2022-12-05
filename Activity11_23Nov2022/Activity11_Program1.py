"""Write a program that takes a text file as input and
prints all unique words in a file in alphabetical order"""

# Input file
fname = input("Enter the file name ")
f = open(fname, 'r')
list1 = list()
words = []
for line in f:
    words += line.split()
words.sort()

for word in words:
    # Check for duplicate words
    if word in list1:
        continue
    else:
        list1.append(word)
        print(word)

# close file
f.close()
