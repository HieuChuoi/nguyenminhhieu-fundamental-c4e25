h1 = int(input("Your Height(cm) = "))
w = int(input("Your Weight(kg) = "))
h = h1 / 100
bmi = w / h**2
print("Your BMI = ",bmi)

if bmi < 16:
    print("Severely underweight")
elif 16 < bmi < 18.5:
    print("Underweight")
elif 18.5 < bmi < 25:
    print("Normal")
elif 25 < bmi < 30:
    print("Overweight")
else:
    print("Obese")