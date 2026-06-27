print("Hello World!")

#indentation
if 5>2:
    print("five is greater the two")


#print statements
#multiple statements
print("Hello My Name is Bhoomika")
print("I am", 21, "years old!")

#python variables
x=5
y="Bhoo"
print(x)
print(y)

#type od datatype
print(type(x))
print(type(y))

#case-sensitive
A=34
a=34
print(A)
print(a)

#many values to multiple variables
x1,y1,z1 = "orange", "apple","kiwi"
print(x1)
print(y1)
print(z1)

#one value to multiple variables
x2=y2=z2 = "Orange"
print(x2)
print(y2)
print(z2)

#unpacking variables
fruits = ["orange", "Kiwi", "Apple"]
x3,y3,z3 = fruits
print(x3,y3,z3)

#global variables
var= "awesome"
def func():
    print("python is " + var)
func()

#local variable
def myfunc():
    var1 = "fantastic"
    print("python is "+ var1)
myfunc()
print("python is " + var)

#global keyword
def my():
    global Key
    Key = "awesome"
    print("python is "+ Key)
my()
print("python is " + Key)
