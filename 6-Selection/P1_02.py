#Q: Minimum of 2 numbers
"""
● Read 2 integers and print the minimum one of them
○ Don’t use min function from python
● Inputs ⇒ outputs
○ 10 20 ⇒ 10
○ 70 5 ⇒ 5
"""

#Answer:
n1,n2 = map(int,input("Enter 2 numbers: ").split())

if n1 > n2:
    print("Min =", n2)
else:
    print("Min =", n1)