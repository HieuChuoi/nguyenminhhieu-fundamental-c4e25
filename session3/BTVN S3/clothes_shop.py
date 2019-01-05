shop = ["T-shirt", "Sweater"]
print('''
R: See all items
C: Add new items
U: Update items
D: Delete items
''')
# s = input("Welcome to our shop, what do you want (C, R, U, D) ?")
loop = True
while loop:
    s = input("Welcome to our shop, what do you want (C, R, U, D) ?")

    if s == "R":
      print("Our items: ", shop)
      loop = True
    elif s == "C":
        c = input("Enter your new item: ")
        shop.append(c)
        print("Our items: ", shop)
        loop = True
    elif s == "U":
        u = input("New items: ")
        shop[1] = u
        print("Our items: ",shop)
        loop = True
    elif s == "D":
        d = input("Delete position: ")
        while not d.isdigit():
            print("Not a number")
            d = input("Delete position: ")
        d1 = int(d)
        shop.pop(d1)
        print("Our items: ",shop)
        loop = True
    else:
        print("Only C, R, U, D")
        loop = True