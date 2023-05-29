print("Welcome to Roller-coaster ride!")
height = int(input("What is your height in cm ? : "))

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age ? : "))

    if age < 12:
        bill = 100
        print("Please pay ₹100")
    elif age <= 18:
        bill = 150
        print("Please pay ₹150")
    else:
        bill = 200
        print("Please pay ₹200")
    
    wants_photo = input("Do you want a photo taken ? y or n  : ")
    if wants_photo == "y":
        bill = bill + 50  # bill += 50
    else:
        print(f"Your bill is ₹{bill}")
    
    print(f"Your total bill is : ₹{bill}")
    
else:
    print("Sorry! You cannot ride the roller-coaster")
