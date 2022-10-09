# Program to reverse kth row in a list
# Method 1: Using reversed() and loop
list1 = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
k = 3
res = []
for i, j in enumerate(list1):
    if (i+1) % k == 0:
        res.append(list(reversed(j)))
    else:
        res.append(j)

print("Original List:", list1)
print("kth rows reversed:", res)
