#Q: Fractional Part
"""
Write a program that reads 2 numbers a, b and divides them (a/b), but prints
only the fraction part
"""

#Answer:
n1, n2 = map(int,input("Enter the 2 numbers: ").split())

print(n1/n2 - n1 // n2)
