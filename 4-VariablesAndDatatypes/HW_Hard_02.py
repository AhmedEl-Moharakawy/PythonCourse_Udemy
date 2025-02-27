#Q: Print Me
"""
● Write a program that reads 2 integers A, B
○ B is either -1 or 1
■ If B is -1, print 2*A+1
■ If B is 1, print A*A
● Input: 7 1 ⇒ 49.0
● Input: 7 -1 ⇒ 15.0
● Hint
○ You need to think in a 1 line formula for the output
"""

#Answer:
A,B = map(int,input().split())

x = 2*A + 1   #if B = -1
y = A*A       #if B = 1

out = ((B - 1)/-2) * x + ((B + 1)/2) * y

print(out)
