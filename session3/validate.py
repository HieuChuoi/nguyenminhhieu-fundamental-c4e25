yob_str = input("Your year of born: ")

while not yob_str.isdigit():
    print("Not a number, enter agian")
    yob_str = input("Your year of born: ")

yob = int(yob_str)
age = 2018 - yob
print(age)