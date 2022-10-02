def binary_search(list1, key):
    low = 0
    high = len(list1)-1
    mid = 0
    while low <= high:
        mid = (low+high)//2
        if key < list1[mid]:
            high = mid - 1
        elif key > list1[mid]:
            low = mid + 1
        else:
            return mid
    return -1


list1 = [1, 2, 3, 4, 5, 6, 7]
print('List:', list1)
key = int(input("Enter the key: "))
res = binary_search(list1, key)
if res == -1:
    print("Element not found!")
else:
    print("Element found at:", res)
