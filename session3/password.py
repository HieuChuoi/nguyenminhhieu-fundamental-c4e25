pass_str = input("Enter password: ")

# while not pass_str.isalnum():
#     print("Password is both number and character")
#     pass_str = input("Enter password: ")

while len(pass_str) < 8 or pass_str.isalpha() or pass_str.isdigit() or (not pass_str.isalnum()) :
    print("Password invalid")
    pass_str = input("Enter password: ")

    

print("Password OK")