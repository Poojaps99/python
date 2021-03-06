def factorial(n):
    fact = 1
    if n == 0:
        print(n, "!=", fact)
    for i in range(1, n + 1):
        fact = i * fact
    print(n, "!=", fact)


n = int(input("Enter the number:"))
factorial(n)
