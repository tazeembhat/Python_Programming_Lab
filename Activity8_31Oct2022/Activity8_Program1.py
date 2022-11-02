# Determine whether the given number is Armstrong number or not.

def order(x):
    count = 0
    while x != 0:
        count += 1
        x = x // 10
    return count


def armstrong(num):
    sum = 0
    temp = num
    n = order(num)
    while num != 0:
        digit = num % 10
        sum = sum + (digit ** n)
        num = num // 10

    if temp == sum:
        return True
    else:
        return False


n = int(input("Enter a number: "))
if armstrong(n):
    print("Number is armstrong.")
else:
    print("Number is not armstrong")
