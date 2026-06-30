username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")

elif username == "admin":
    print("Wrong Password")

else:
    print("User Not Found")