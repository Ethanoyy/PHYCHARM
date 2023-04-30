
def CalcuBMI(x, y):
    print("Height = " + str(x))
    print("Weight = " + str(y))
    BMI = (y / (x * x))
    print("BMI = " + str(BMI))

    if (BMI < 18.5):
        print("UNDERWEIGHT")

    elif (BMI <= 25.0) and (BMI>=18.5):
        print("Normal weight")

    else:
        print("OVERWEIGHT")

CalcuBMI(1.8, 65)



