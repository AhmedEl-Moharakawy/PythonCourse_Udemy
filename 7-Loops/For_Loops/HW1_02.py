#Q: Find Special Pairs
"""
● Count How many X, Y numbers such that
○ X in range [50-300]
○ Y in range [70-400]
○ X < Y
○ (X+Y) divisible by 7
● Output
○ 8040
● After solving, think in minor optimizations
"""

#Answer:
x1,y1,x2,y2 = map(int,input("Enter pairs: ").split())
count = 0

for x in range(x1,y1+1,1):
    for y in range(x2,y2+1,1):
        if (x < y) and ((x + y) % 7 == 0):
            count += 1 

print("Counts =",count)