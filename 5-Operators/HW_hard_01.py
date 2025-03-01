#Q:
"""
Write a program that reads an integer and print 100 if number is even or 7 if
number is odd
○ E.g. for input 8 ⇒ 100
○ E.g. for input 133 ⇒ 7
"""

#Answer:
num = int(input("Enter a number: "))

print(7 * bool(num % 2) + 100 * (not bool(num % 2)))