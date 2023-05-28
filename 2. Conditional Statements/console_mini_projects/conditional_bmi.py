# Conditional BMI calculator.

height = float(input("Enter your height in metres : "))
weight = int(input("Enter your weight in kilograms : "))

bmi = weight / height ** 2
rounded_bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your bmi is {rounded_bmi}, you are underweight!")
elif bmi < 25:
    print(f"Your bmi is {rounded_bmi}, you have normal weight.")
elif bmi < 30:
    print(f"Your bmi is {rounded_bmi}, you are overweight!")
elif bmi < 35:
    print(f"Your bmi is {rounded_bmi}, you are obese!")
else:
    print(f"Your bmi is {rounded_bmi}, you are clinically obese!")

