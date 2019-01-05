from random import randint

x = randint(1, 100)
# print(x)

n = int(input("Your guess: "))
while x != n:
    if n > x:
        print("A little too big")
    elif n < x:
        print("a little too small")
    n = int(input("Your guess: "))
print("BINGO")