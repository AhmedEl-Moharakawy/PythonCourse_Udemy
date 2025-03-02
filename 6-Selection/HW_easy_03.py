#Q: Maximum but constrained
"""
● Given 3 integers, you have to find the biggest one of them which is < 100.
○ Print -1 if no such number
● Inputs
○ 22 90 115 ⇒ 90
■ Here [20 90] are only < 100. Maximum (20, 90) = 90
○ 200 300 400 ⇒ -1
■ All of them are > 100, so no answer
○ 50 100 150 ⇒ 50
■ Only 50 is < 100.
○ 10 30 20 ⇒ 30
■ The 3 numbers < 100, so their max is 30
"""

#Answer:
n1,n2,n3 = map(int,input("Enter 3 numbers: ").split())
max = -1
if n1 > 100:
    n1 = -1

if n2 > 100:
    n2 = -1

if n3 > 100:
    n3 = -1

if n1 > max and n1 > n2 and n1 > n3:
    max = n1
elif n2 > max and n2 > n1 and n2 > n3:
    max = n2
elif n3 > max and n3 > n1 and n3 > n2:
    max = n3
else:
    max = -1

print("Maximum =",max)