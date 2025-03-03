#Q: Print Range
"""
● Given a starting integer X and an ending integer Y, print all integers between
X and Y inclusive, each on a line.
● Input 3 7
● Output
○ 3
○ 4
○ 5
○ 6
○ 7
"""

#Answer:
x, y = map(int, input("Enter start and end: ").split())

if x > y:
    print("Invalid")
else:
    while x <= y:
        print(x)
        x += 1
