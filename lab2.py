
def CalcuBMI(x, y):
    print("Height = " + str(x))
    print("Weight = " + str(y))
    BMI = (y / (x * x))
    print("BMI = " + str(BMI))

    if (BMI < 18.5):
        print("UNDERWEIGHT")
        return -1

    elif (BMI <= 25.0) and (BMI>=18.5):
        print("Normal weight")
        return 0

    else:
        print("OVERWEIGHT")
        return 1

CalcuBMI(1.8, 65)



