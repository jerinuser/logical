import re 

password = input("enter your password:")

def passw():
    if len(password) < 8:
        print("password must be 8 characteristics long")
    elif not re.search(r"[A-Z]",password):
        print("password must contain atleast one uppercases letters")
    elif not re.search(r"[a-z]",password):
        print("password must contain atleast one small letters")
    elif not re.search(r"[!@#$%^&*]",password):
        print("password must contain atleast one special characters")
    elif not re.search(r"[0-9]",password):
        print("password must contain atleast one digit")
    elif " " in password:
        print("Password must not contain spaces.")
    else: 
        print("password denied")

passw()
        