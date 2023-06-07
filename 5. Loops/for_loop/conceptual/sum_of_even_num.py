# Sum of all even numbers from the range 1 to 100.

# Method 1 :

total = 0
for number in range(2, 101, 2):
    total += number
print("Method 1 : ", total) # 2550

# Method 2 :

total_2 = 0
for number_2 in range(1, 101):
    if number_2 %2 == 0:
        total_2 += number_2
print("Method 2 : ", total_2) # 2550
