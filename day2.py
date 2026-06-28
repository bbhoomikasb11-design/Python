#operators

#arithmetic operators
a=10
b=30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#comparision operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

#ternary operators
num = 6
s= "WEEKDAY" if num<=5 else "WEEKEND"
print(s)

#logical operators
print(a>5 and b<3)
print(a>5 or b<3)
print(not(a>4))

#identity operators
print(a is b)
print(a is not b)

#membership operators
x = ["banana", "apple", "orange"]
print("banana" in x)
print("pineapple" not in x)

#bitwise operator
print(6&3)
print(6|3)
print(6^3)
print(~6)

#operator precedence
print((100+1)-(100+1))
print(5+4-6+4*6)

#type casting
a=10
b=float(a)
print(b)
print(type(b))

c=10.45
d=int(a)
print(d)
print(type(d))

e="100"
f=int(e)
print(f)
print(type(f))