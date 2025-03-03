#Q: Triples of numbers

"""
● Read integers N, M, W.
● Find the total number of triples that
has A + B <= C where
○ 1 <= A <= N
○ A <= B <= M
○ 1 <= C <= W
● Input: 100 200 20
● Output: 715
● Stop video and code
"""

#Answer:

n,m,w = map(int,input("Enter N, M, Sum: ").split())
count = 0
for i in range(1,n+1):
    for j in range(i,m+1):
        for k in range(1,w+1):
            if i+j <= k:
                count += 1 

print("Count =",count)

#another way for large numbers
print("-"*20)
print("Another way")
print("-"*20)

n,m,w = map(int,input("Enter N, M, Sum: ").split())
count = 0

for i in range(1,n+1):
    for j in range(i,m+1):
        k = i+j
        if 1 <= k <= w:
            count += w - k + 1 

print("Count =",count)