#####################################################################################
# Tip calculator in python.

print("Welcome to the Tip calculator!")
print()

bill = float(input("What was your Total Bill amount? : ₹"))
tip = int(input("How much '%' of Tip would you like to give ? 10, 12 or 15 ? :"))
people = int(input("How many people would like to split the bill : "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay : [₹{final_amount}]")
#####################################################################################
