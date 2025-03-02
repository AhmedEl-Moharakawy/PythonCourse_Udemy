#Q: Find Maximum of 10 numbers
"""
● Read 10 numbers and find which of them has the biggest value and print it.
● Inputs (each integer on a seperate line)
○ 1
○ 67
○ -9
○ 88
○ -45
○ 129
○ 90
○ 65
○ 77
○ 34
● Output ⇒ 129
● Restriction: In your whole code there should be 2 variables defined ONLY
"""

#Answer:
num = int(input("Enter Number 1: "))
max = num

num = int(input("Enter Number 2: "))
if num > max:
    max = num

num = int(input("Enter Number 3: "))
if num > max:
    max = num

num = int(input("Enter Number 4: "))
if num > max:
    max = num

num = int(input("Enter Number 5: "))
if num > max:
    max = num

num = int(input("Enter Number 6: "))
if num > max:
    max = num

num = int(input("Enter Number 7: "))
if num > max:
    max = num

num = int(input("Enter Number 8: "))
if num > max:
    max = num

num = int(input("Enter Number 9: "))
if num > max:
    max = num

num = int(input("Enter Number 10: "))
if num > max:
    max = num

print("Max = ", max)