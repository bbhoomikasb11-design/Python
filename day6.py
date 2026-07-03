def table():
    num = 5
    print(f"Table of {num}")
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# 6. Factorial
def factorial():
    n = 5
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)