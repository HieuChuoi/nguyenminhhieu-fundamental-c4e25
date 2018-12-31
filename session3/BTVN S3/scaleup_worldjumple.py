game = ["meticulous", "champion", "hexagon"]
from random import randint
game_len = int(len(game))
game_index = randint(0, game_len - 1)

answer = game[game_index]
letter = list(answer)
# print(answer)
# print(letter)
print("Guess this word:")
for i in range(len(letter)):
    b = randint(0, len(letter) - 1)
    word = letter[b]
    letter.pop(b)
    print((word),end=' ')

print()

a = input("Your answer: ")
while a!= answer:
    print(":(")
    a = input("Your answer: ")
print("Hura")