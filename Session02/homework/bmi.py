height = int(input("nhap chieu cao cua ban(cm): "))
weight = float(input("nhap can nang(kg): "))

height_m = height/100
bmi = weight/(height_m**2)

if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")