two_digit_num = input("Enter a 2 digit number : ")
print()
'''
THIS PROVIDES A 'STRING' OUTPUT: 

first_digit = two_digit_num[0]
print(first_digit)
second_digit = two_digit_num[1]
print(second_digit)
'''

# explicit type casting of the 2 digits:
int_first_digit = int(two_digit_num[0])
print("The first digit is : ", int_first_digit)

int_second_digit = int(two_digit_num[1])
print("The second digit is : ", int_second_digit)
print()

# result
result = int_first_digit + int_second_digit
print("The sum of the 2 digits is : " , result)
