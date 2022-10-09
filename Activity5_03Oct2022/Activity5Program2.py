# Program to reverse kth row in a list
# Method 2: Using Slicing and list comprehension
list1 = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
k = 3
res = [ele[::-1] if (idx + 1) % k == 0 else ele for idx, ele in enumerate(list1)]

print("Original List:", list1)
print("kth rows reversed:", res)
