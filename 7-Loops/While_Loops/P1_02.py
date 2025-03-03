#Q: Power Function
"""
● Read 2 integers X and Y and compute X**Y.
○ This means X * X * X ….. Y times
○ E.g = 25= 2 * 2 * 2 * 2 * 2
● Note: Don’t use X ** Y
○ Implement yours
"""

#Answer:
x,y = map(int,input("Enter the 2 numbers: ").split())

count = 0
power = 1

if y == 0:
    power = 1
else:
    if y < 0:
        y = -y
        while count < y:
            power *= x
            count += 1
            power = 1 / power
    else:
        while count < y:
            power *= x
            count += 1

print(x,"to the power of",y,"=",power)
