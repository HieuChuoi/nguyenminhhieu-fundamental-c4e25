a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("a*x**2 + b*x + c = 0")


if a == 0:
    print("Phuong trinh co mot nghiem duy nhat")
    x = -c / b
    print("x = ",x)
else:
    d = b**2 - 4*a*c
    if d == 0:
        print("Phuong trinh co nghiem kep")
        x = -b / (2*a)
        print("x = ",x)
    elif d < 0:
        print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co hai nghiem phan biet")
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print("x1 = ",x1)
        print("x2 = ",x2)