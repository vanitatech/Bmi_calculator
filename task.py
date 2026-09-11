weight = int(input("Enter your weight: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")

elif bmi < 25:
    print("normal weight")

elif bmi >= 25:
    print("overweight")

