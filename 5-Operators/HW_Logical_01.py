#Q: Create logic!
"""
● Write a program that reads 3 integers about the class room
○ Number of boys (nb), number of girls (ng), number of teachers (nt)
● Prepare and print a boolean variable for these cases:
● nb greater than 25
● ng less than or equal to 30
● nb > 20 and nt > 2 or ng > 30 and nt > 4
● Either nb < 60 or ng < 70
● Neither nb >= 60 nor ng >= 70
● nb is 10 more students than ng
● Difference between nb and ng is more than 10 or nt > 5
● Either nb is 10 more students than ng or ng is 15 more students than nb
"""

#Answer:
nb = int(input("Enter the number of boys: "))
ng = int(input("Enter the number of girls: "))
nt = int(input("Enter the number of teachers: "))

print(bool(nb > 25))
print(bool(ng <= 30))
print(bool(nb > 20 and nt > 2 or ng > 30 and nt > 4))
print(bool(nb < 60 or ng < 70))
print(bool(not nb >= 60 and not ng >= 70))
print(bool(nb == ng + 10))
print(bool(nb - ng < 10 or nt > 5))
print(bool(nb == 10 + ng or ng == nb + 15))