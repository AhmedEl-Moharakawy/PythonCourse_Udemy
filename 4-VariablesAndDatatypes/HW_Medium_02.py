#Q: Swapping 2 numbers!
"""
● Write a program that reads 2 integers num1 and num2
○ E.g. say we read num1 = 7 and num2 = 25
● Target: we want swap the values of num1 and num2?
○ Swap means exchange
○ So Num1 has value 25 and Num2 has value 7
○ Write 3 lines of code only
"""

#Answer:
num1, num2 = map(int,input().split())

num3 = num1 
num1 = num2
num2 = num3
print(num1,num2)