def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


list1 = [3, 5, 1, 4, 2]
print(insertion_sort(list1))
