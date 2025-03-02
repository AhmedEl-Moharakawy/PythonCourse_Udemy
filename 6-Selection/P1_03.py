#Q: Minimum of 3 numbers
"""
● Read 3 numbers and print the minimum one of them
● Inputs
○ 10.5 20 30 ⇒ 10.5
○ 70 5 15 ⇒ 5
solve it in 3 different ways
"""

#Answer:
n1,n2,n3 = map(int,input("Enter 3 numbers: ").split())

#1st way
if n1 < n2:
    if n1 < n3:
        print("Min =", n1)
    else:
        print("Min", n3)
elif n2 < n3:
    print("Min =", n2)
else:
    print("Min", n3)

#2nd way
if (n1 < n2) and (n1<n3):
    print("Min:",n1)
elif (n2 < n1) and (n2 < n3):
    print("Min:",n2)
else:
    print("Min:",n3)

#3rd way
min = n1
if (min > n2):
    min = n2

if (min > n3):
    min = n3

print("Min =",min)