# Program to create a list of student's records and search a student record using a dictionary.
#  Creating Dictionary
students = dict()
n = int(input("Enter the number of students: "))
for i in range(n):
    sname = input("Enter the name of a student: ")
    marks = []
    s = 3
    for j in range(s):
        m = float(input("Enter marks: "))
        marks.append(m)
        students[sname] = marks
print("Student Dictionary Created: ")
print(students)

# Searching Dictionary
print("Search Records:")
name = input("Enter the name of Student: ")
if name in students.keys():
    print(students[name])
else:
    print("No Records found!")
