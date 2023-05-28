# Your life in weeks (until the age 90)

age = int(input("What is your age : "))

# until the age 90
years_remaining = 90 - age
# 12 months in a year
months_remaining = years_remaining * 12
# 52 weeks in a year
weeks_remaining = years_remaining * 52
# 365 days in a year
days_remaining = years_remaining * 365

message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months and {years_remaining} years remaining until the age 90"
print(message)
