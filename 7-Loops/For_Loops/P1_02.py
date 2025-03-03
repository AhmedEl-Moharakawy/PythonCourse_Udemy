#Q: Pair of numbers
"""
● Read 3 integers N, M, SUM.
● Find total number of pairs that satisfy
A + B == SUM where
○ 1 <= A <= N
○ 1 <= B <= M
● Stop video and code
● Input ⇒ Output
○ 200 300 70 ⇒ 69
● What about input?
○ 1000000 1000000 1000000
○ How many steps the code do?
"""

#Answer:
n,m,sum = map(int,input("Enter N, M, Sum: ").split())
count = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if i+j == sum:
            count += 1 

print("Count =",count)


#another way for large numbers
print("-"*20)
print("Another way")
print("-"*20)

n,m,sum = map(int,input("Enter N, M, Sum: ").split())
count = 0
for i in range(1,n+1):
    j = sum - i
    if j >= 1 and j <= m:
        count += 1

print("Count =",count)