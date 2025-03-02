#Q: Conditional Count
"""
● Write a program that reads number X, then other 5 numbers. Print 2 values:
○ How many numbers <= X
○ How many numbers > X
○ Any relation between these 2 outputs?
● Inputs
○ 10 300 1 5 100 200
○ Output: 2 3
○ Explantation
○ 2 numbers (1, 5) are <= 10
○ 3 numbers (100, 200, 300) are > 10
"""

#Answer:
x = int(input("Enter X: "))
n1,n2,n3,n4,n5 = map(int,input("Enter 5 numbers: ").split())

count_greater = 0

if n1 > x:
   count_greater += 1

if n2 > x:
   count_greater += 1

if n3 > x:
   count_greater += 1

if n4 > x:
   count_greater += 1

if n5 > x:
   count_greater += 1

print("Greater =",count_greater,"\nLess =",5 - count_greater)