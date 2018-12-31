loop = True
while loop:
    pwd = input("Enter your password: ")
    loop = False #assume password is valid
    if len(pwd) < 8:
        print("Password length must be greater than 8")
        loop = True
    if not pwd.isalnum():
        print("Password must not contain special characters")
        loop = True
    if pwd.isdigit():
        print("Password must contain letters")
        loop = True
    if pwd.isalpha():
        print("Password must contain digits")
        loop = True
        
print("Password OK")