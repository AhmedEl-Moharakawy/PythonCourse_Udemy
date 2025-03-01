#Q: Averages
"""
Write a program that reads 5 numbers and print the following:
○ A) Their average
○ B) The sum of the first 3 numbers divided by the sum of the last 2 numbers
○ C) The average of the first 3 numbers divided by the average of the last 2 numbers.
○ What is the math relation between B and C?
"""

#Answer:
n1,n2,n3,n4,n5 = map(float,input("Enter 5 Numbers: ").split())

av_5 = (n1+n2+n3+n4+n5)/5
print("Their average =", av_5)

sum_first_3 = n1+n2+n3
sum_last_2 = n4+n5

print("The sum of the first 3 numbers / The sum of the last 2 numbers =", sum_first_3/sum_last_2)
print("The average of the first 3 numbers / the average of the last 2 numbers =", (2/3)*( sum_first_3/sum_last_2))
