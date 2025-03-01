#Q: 4th digits from the end
"""
Write a program that reads an integer and print the 4th from the right side. If
no such digit, print 0
"""

#Answer:
num = int(input("Enter a number: "))
temp = num

dig = temp % 10 #1st_digit
temp //= 10

dig = temp % 10 #2nd_digit
temp //= 10

dig = temp % 10 #3rd_digit
temp //= 10

dig = temp % 10 #3rd_digit
temp //= 10

print("4th Digit =",dig)
