# Create a text file and ask the user to write separate 3 lines with three input statements.

fname = open("sampleFile.txt", 'w+')
print("Enter three lines")
i = 1
while i <= 3:
    data = input()
    fname.write(f"{data}\n")
    i += 1
fname = open("sampleFile.txt")
data = fname.read()
print(data)
fname.close()