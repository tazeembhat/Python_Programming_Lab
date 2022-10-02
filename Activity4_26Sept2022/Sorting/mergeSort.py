def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                unsorted_list[k] = left[i]
                i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            unsorted_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_list[k] = right[j]
            j += 1
            k += 1


list1 = [5, 9, 7, 8, 3, 1, 2, 6, 10, 4]
merge_sort(list1)
print(list1)
