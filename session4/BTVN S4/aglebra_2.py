print('''
Answer the following aglebra question:
If x = 8, then what is the value of 4(x+3) ?
''')
answer = [35, 36, 40, 44]
for index, item in enumerate(answer):
    print(index + 1, item, sep=". ")
print()
n = int(input("Your choice: "))
if n != 4:
    print(":(")
elif n == 4:
    print("Bingo")
else:
    pass

print()

print('''
Estimate this answer (exact calculation not needed)
Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?
''')
answer_2 = ["About 55", "About 65", "About 75", "About 85"]
for index, item in enumerate(answer_2):
    print(index +1, item, sep=". ")
print()
m = int(input("Your choice: "))
if m != 2:
    print(":(")
elif m ==2:
    print("Bingo")
else:
    pass

print()

if n == 4 and m == 2:
    print("You correctly answer 2 out of 2 questions")
elif n != 4 or m != 2:
    print("You correctly answer 1 out of 2 questions")
elif n != 4 and m !=2:
    print("You corrertly answer 0 out of 2 questions")