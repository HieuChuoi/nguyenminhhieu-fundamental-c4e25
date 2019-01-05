sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hieu and this are my ship size ",end='')
print(sheep)

print()

biggest_sheep = max(sheep)
print("Now my biggest sheep has size ",biggest_sheep," let's shear it")

print()

sheep[2] = 8
print("After shearing, here is my flock ",sheep)

print()

z = int(len(sheep))
for i in range(z):
    sheep[i] += 50
print("One month has passed, now here is my flock: ",end='')
print(sheep)