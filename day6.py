def table():
    num = 5
    print(f"Table of {num}")
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

def factorial():
    n = 5
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)

    
def reverse_string():
    text = "Python"
    print("Reversed String:", text[::-1])

def count_vowels():
    text = "Hello World"
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    print("Vowels:", count)