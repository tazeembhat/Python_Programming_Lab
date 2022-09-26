def linear_search(list1, n, key):
    for i in range(0, n):
        if key == list1[i]:
            return i
    return -1


def main():
    list1 = [2, 5, 6, 1, 3, 4]
    n = 6
    print('List:', list1)
    key = int(input("Enter the key."))
    res = linear_search(list1, n, key)
    if res == -1:
        print("Element not found!")
    else:
        print("Element found at:", res)


if __name__ == "__main__":
    main()
