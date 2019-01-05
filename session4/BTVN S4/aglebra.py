print('''
Answer the following aglebra question:
If x = 8, then what is the value of 4(x+3) ?
''')
answer = [35, 36, 40, 44]
for index, item in enumerate(answer):
    print(index + 1, item, sep=". ")
print()
n = int(input("Your choice: "))
while True:
    if n != 4:
        print(":(")
        n = int(input("Your choice: "))
    elif n == 4:
        print("Bingo")
        break
    else:
        pass