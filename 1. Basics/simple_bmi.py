# Simple BMI calculator 

height = input("Enter your height in metres : ")
weight = input("Enter your weight in kgs : ")

bmi = int(weight) / float(height) ** 2

int_bmi = int(bmi)
print("Your body mass index is : ", int_bmi)
