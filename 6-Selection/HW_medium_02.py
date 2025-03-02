#Q: Find Maximum up to 10 numbers
"""
● Read an integer N (1 <= N <= 10)
● Then read N numbers, find which of them has the biggest value and print it.
● Inputs (but they will be on seperate lines)
○ 5 1 3 2 4.5 2 ⇒ 4.5
■ 5 means read 5 integers
■ Then we read them [1 3 2 4.5 2]. Their maximum is 4.5
○ 10 1 67 -9 88 -45 129 90 65 77 34 ⇒ 129
■ Same as last homework. This time we are given first N (10)
"""

#Answer:
N = int(input("Enter the number of numbers: "))
count_inputs = 0
num = float(input("Enter the number 1: "))
max = num
count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 2: "))
    count_inputs += 1
    if num > max:
        max = num

if count_inputs < N:
    num = float(input("Enter the number 3: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 4: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 5: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 6: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 7: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 8: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 9: "))
    if num > max:
        max = num
    count_inputs += 1

if count_inputs < N:
    num = float(input("Enter the number 10: "))
    if num > max:
        max = num
    count_inputs += 1

print("Max = ", max)
