def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j+1]


list1 = [5, 7, 3, 4, 1, 0]
bubble_sort(list1)
print(list1)
