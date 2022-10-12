# Program to perform a Linear Search
def linear_search(arr, size, key):
    for i in range(size):
        if arr[i] == key:
            return i
    return -1


n = int(input("Enter the size of list: "))
list1 = []

for i in range(0, n):
    x = int(input("Enter Element: "))
    list1.append(x)
print("The given list is:", list1)

k = int(input("Enter the element to Search: "))
ret = linear_search(list1, n, k)

if ret == -1:
    print("Element not found!")
else:
    print("Element found at location:", ret)

