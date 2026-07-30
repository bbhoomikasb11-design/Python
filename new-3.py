a = 10
b=15
print(a)
print(b)
a,b = b,a
print(a)
print(b)

c= 30
d=40
print(c)
print(d)
temp = c
c = d
d = temp
print(c)
print(d)

name = input("enter your name: ")
marks1 = int(input(" enter marks for subject 1: "))
marks2 = int(input(" enter marks for subject 2: "))
marks3 = int(input(" enter marks for subject 3: "))
marks4 = int(input(" enter marks for subject 4: "))
marks5 = int(input(" enter marks for subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
avg = total/2
print(f"Total marks of {name}is {total} and the average marks is {avg}")
