def linear_search(arr, size, k):
    for i in range(0, size):
        if k == arr[i]:
            return i
    return -1


list1 = [2, 5, 6, 1, 3, 4]
n = 6
print('List:', list1)
key = int(input("Enter the key."))
res = linear_search(list1, n, key)
if res == -1:
    print("Element not found!")
else:
    print("Element found at:", res)
