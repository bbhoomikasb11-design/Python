number = int(input("enter a number: "))
if number > 0:
    print("the number is a positive number")


age = int(input("enter the age :"))
if age >=18:
    print("eligible to vote")
else:
    print("not eligible")


num = int(input("enter a number: "))
if num % 2 == 0:
    print(" even")
else:
    print("Odd")


first_number = int(input("enter a number:"))
second_number = int(input("enter next number: "))
if first_number > second_number:
    print(" First number is larger")
else:
    print(" second number is larger")


marks = int(input("enter the marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("Fail")


num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"Largest number is {num1}")
elif num3 >= num1 and num3 >= num2:
    print(f" Largest number is {num3}")
else:
    print(f"Largest number is {num2}") 