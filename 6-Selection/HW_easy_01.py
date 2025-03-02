#Q: Arithmetic
"""
● Read 2 integers A, B and print based on following cases:
○ if both are odd print their product A*B
○ if both are even print their division A/B (float division / assume B != 0)
○ if the first is odd and the second is even then find their sum A+B
○ if the first is even and the second is odd then find their subtraction A-B
● Inputs ⇒ outputs
○ 5 7 => 35
○ 12 2 => 6
○ 5 6 => 11
○ 12 3 => 9
"""

#Answer:
A,B = map(int,input("Enter 2 numbers: ").split())
A_isOdd = A % 2
B_isOdd = B % 2

if A_isOdd and B_isOdd:
    print("A*B=",A*B)
elif (not A_isOdd) and (not B_isOdd):
    print("A/B=",A/B)
elif A_isOdd and (not B_isOdd):
    print("A+B=",A+B)
else:
    print("A-B=",A-B)
