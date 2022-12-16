# Program to convert Roman numerals into Integers

def value(roman):
    if roman == 'I' or 'i':
        return 1
    if roman == 'V' or 'v':
        return 5
    if roman == 'X' or 'x':
        return 10
    if roman == 'L' or 'l':
        return 50
    if roman == 'C' or 'c':
        return 100
    if roman == 'D' or 'd':
        return 500
    if roman == 'M' or 'm':
        return 1000
    return -1


# Function to convert roman number into decimal
def roman_to_decimal(str1):
    res = 0
    i = 0

    while i < len(str1):
        s1 = value(str1[i])

        if i+1 < len(str1):
            s2 = value(str1[i+1])

            if s1 >= s2:
                res = res + s1
                i = i+1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res


r = input("Enter the Roman Number:")
print("Decimal value = ", roman_to_decimal(r))
