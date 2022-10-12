# Program to print Fibonacci series
def fibonacci(n):
    t1 = 0
    t2 = 1
    print(t1, t2, end=" ")
    for i in range(2, n):
        nextTerm = t1 + t2
        t1 = t2
        t2 = nextTerm
        print(nextTerm, end=" ")
    return


n = int(input("Enter the number of terms: "))
fibonacci(n)
