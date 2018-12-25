from turtle import*

shape("turtle")
speed(0)

d = 100
# for i in range(1, 300, 1):
#     forward(i)
#     left(90)
for i in range(20):
    forward(d)
    left(90)
    d += 10
    #d += 1, d -= 5, d *= 2, d /= 2
    #d = d + 1

mainloop()