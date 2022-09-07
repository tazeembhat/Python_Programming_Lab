# Python function to sum all the number in a list

list1 = [1, 2, 3, 4, 5, 6]


def list_sum(list1):
    Sum = 0
    for i in list1:
        Sum += i
    print("Sum = ", Sum)


list_sum(list1)
