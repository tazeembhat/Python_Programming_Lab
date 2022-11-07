# Sum of number digits in List

sample_list = [12, 22, 32, 42, 52]
print("Original List: " + str(sample_list))

res = []
for ele in sample_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)

print("The sum of number digit in list = ", res)
