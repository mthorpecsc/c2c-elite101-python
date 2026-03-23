import time

def BMI():
    print('This is a BMI Calculator')

    while True:
        weight = (input("Enter your weight (in kilograms): "))
        height = (input("Enter in your height (in meters): "))

        if weight.isalpha() or height.isalpha() == False:
            bmi_calculator(weight, height)
            break
        else:
            print("Please type in numerical values only.")
            print("-"*30)

def bmi_calculator(weight, height):
    weight = float(weight)
    height = float(height)

    user_bmi = weight / (height ** 2)
    rounded_bmi = round(user_bmi, 6)
    print("Calculating BMI....")
    time.sleep(3)

    print(rounded_bmi)

    if rounded_bmi < 18.5:
        print("You're classified as underweight")
    elif 18.5 <= rounded_bmi <= 25:
        print("You're classified as healthy weight")
    elif 25 < rounded_bmi < 30:
        print("You're classified as overweight")
    elif 30.0 < rounded_bmi:
        print("You're classified as obese")

BMI()
