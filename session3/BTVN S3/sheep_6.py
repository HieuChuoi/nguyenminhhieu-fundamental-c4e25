sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hieu and this are my ship size ",end='')
print(sheep)
biggest_sheep = max(sheep)
print("Now my biggest sheep has size ",biggest_sheep," let's shear it")
sheep[2] = 8
print("After shearing, here is my flock ",sheep)

z = int(len(sheep))
for i in range(z):
    sheep[i] += 50
print("One month has passed, now here is my flock: ",end='')
print(sheep)
biggest_sheep = max(sheep)
print("Now my biggest sheep has size ",biggest_sheep," let's shear it")
sheep[3] = 8
print("After shearing, here is my flock ",sheep)

z = int(len(sheep))
for i in range(z):
    sheep[i] += 50
print("One month has passed, now here is my flock: ",end='')
print(sheep)
biggest_sheep = max(sheep)
print("Now my biggest sheep has size ",biggest_sheep," let's shear it")
sheep[6] = 8
print("After shearing, here is my flock ",sheep)

z = int(len(sheep))
for i in range(z):
    sheep[i] += 50
print("One month has passed, now here is my flock: ",end='')
print(sheep)

s = sum(sheep)
print("My flock has size in total: ",s)
money = s * 2
print("I would get: ",s," * 2$ = ",money,"$")