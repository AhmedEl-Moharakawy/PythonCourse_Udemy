#Q: Swapping 3 numbers!
"""
● Write a code to swap 3 numbers
● Let say we have numbers a = 115, b = 20, c = 301
● We wanna their final values to be: a = 20, b = 301, c = 115
"""

#Answer:

num1, num2, num3 = map(int,input("Enter the 3 numbers: ").split())

num4 = num1
num1 = num2
num2 = num3
num3 = num4

print(num1,num2,num3)
