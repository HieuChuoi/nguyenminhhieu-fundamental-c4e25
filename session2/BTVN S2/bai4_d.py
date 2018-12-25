n = int(input("n = "))
for i in range(0, n):
    if i % 2 == 0:
        print("x",end='')
    elif i % 2 == 1:
        print("*",end='')
    else:
        pass
