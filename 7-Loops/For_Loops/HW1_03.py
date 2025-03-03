#Q: Find all quadruples
"""
● Count how many integer (a, b, c, d) with the following property:
○ 1 <= a, b, c, d <= 200
○ a + b = c + d
● Output:
○ 5333400
● Code it once using 4 loops (very slow!)
● Code it once using 3 loops only
● In future: you can do it using 2 loops only!
"""

#Answer:

#solution_way_1
count = 0

for a in range(1,201,1):
    for b in range(1,201,1):
        for c in range(1,201,1):
            for d in range(1,201,1):
                if a + b == c + d:
                    count += 1

print("Count =",count)

count = 0
#solution_way_2
for a in range(1,201,1):
    for b in range(1,201,1):
        for c in range(1,201,1):
            d = a + b - c
            if d >= 1 and d <= 200:
                count += 1

print("Count =",count)
