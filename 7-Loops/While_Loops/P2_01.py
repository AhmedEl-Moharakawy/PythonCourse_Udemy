#Q: Number of digits
"""
● Read an integer and count its number of
digits
● See the output screenshot
● Note: one trivial way is to convert the
number to string
○ Don’t use strings
"""

#Answer:
num = int(input("Enter a number: "))
temp = num
count = 0

if temp <= 0:
    if temp == 0:
        count = 1
    else:
        temp = -temp

while temp > 0:
    count += 1
    temp //= 10

print("The number",num,"is",count,"digits.")