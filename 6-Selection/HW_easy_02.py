#Q: Sort 3 numbers
"""
● Given 3 integers, sort (order) them in ascending order and print them .
● Inputs ⇒ outputs
○ 1 2 3 ⇒ 1 2 3
○ 1 3 2 ⇒ 1 2 3
○ 2 1 3 ⇒ 1 2 3
○ 2 3 1 ⇒ 1 2 3
○ 3 1 2 ⇒ 1 2 3
○ 3 2 1 ⇒ 1 2 3
● Do you notice there are only 6 ways to permutate 3 numbers!
"""

#Answer:
n1,n2,n3 = map(int,input("Enter 3 numbers: ").split())
t1,t2,t3 = 0, 0, 0

if (n1 < n2) and (n1 < n3):
    t1 = n1
    if(n2 < n3):
        t2 = n2
        t3 = n3
    else:
        t2 = n3
        t3 = n2
elif (n2 < n1) and (n2 < n3):
    t1 = n2
    if(n1 < n3):
        t2 = n1
        t3 = n3
    else:
        t2 = n3
        t3 = n1
else:
    t1 = n3
    if(n2 < n1):
        t2 = n2
        t3 = n1
    else:
        t2 = n1
        t3 = n2

print("Numbers arranged:",t1,t2,t3)