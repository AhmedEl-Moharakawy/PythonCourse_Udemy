#Q: Our remainder
"""
Write a program that reads 2 positive integers and print such reminder without
using the modulus operator %
"""

#Answer:
n1, n2 = map(int,input("Enter the 2 numbers: ").split())

div = n1 // n2

rem = n1 - div*n2

print("Reminder =", rem)