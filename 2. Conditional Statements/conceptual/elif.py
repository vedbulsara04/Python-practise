print("Welcome to Roller-coaster ride!")
height = int(input("What is your height in cm ? : "))

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age ? : "))

    if age < 12:
        print("Please pay ₹100")
    elif age <= 18:
        print("Please pay ₹150")
    else:
        print("Please pay ₹200")
    
else:
    print("Sorry! You cannot ride the roller-coaster")

