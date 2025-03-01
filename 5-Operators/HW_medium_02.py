#Q: Last 3 digits sum
"""
Write a program that reads an integer and 
prints the sum of its last 3 digits.
"""

#Answer:
num = int(input("Enter a number: "))
temp = num

sum = temp % 10 #1st_digit
temp //= 10

sum += temp % 10 #2nd_digit
temp //= 10

sum += temp % 10 #3rd_digit
temp //= 10

print("Sum =",sum)