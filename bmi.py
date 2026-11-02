def calculate_bmi(height, weight):

    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)

    print("BMI = ", f"{bmi:.2f}")
    if bmi<18.5:
        print("Under Weight") #-1
        return -1
    elif bmi>25.0:
        print("Over Weight") #1
        return 1
    else:
        print("Normal Weight") #0
        return 0


print("=====================")
calculate_bmi(weight=27, height=1.73)
print("=====================")
calculate_bmi(weight=57, height=1.73)
print("=====================")
calculate_bmi(weight=97, height=1.73)
print("=====================")