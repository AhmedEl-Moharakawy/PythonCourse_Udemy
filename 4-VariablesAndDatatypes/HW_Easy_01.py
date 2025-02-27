#Q: Write a program that reads 2 numbers and print their + - * / computations
"""
# ● Do good testing for your code
# ○ E.g. consider negative values
# ○ E.g. even and odd values
# ○ E.g. consider zero as first or 2nd number
"""

#Answer:
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print(n1, "+", n2, "=", n1+n2)
print(n1, "-", n2, "=", n1-n2)
print(n1, "*", n2, "=", n1*n2)
print(n1, "/", n2, "=", n1/n2)

print("End of program")