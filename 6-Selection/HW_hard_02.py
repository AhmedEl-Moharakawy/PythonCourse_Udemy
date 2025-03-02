
#Q: Two Intervals Intersection
"""
● Read 4 integers representing 2 intervals and print their intersection interval. If
they don’t intersect, print -1
● Inputs
○ 1 6 3 8 ⇒ 3 6
■ Interval [1 6] and [3 8] only intersects at [3, 6]
■ Why: interval [1, 6] has numbers: {1, 2, 3, 4, 5, 6}
■ And: interval [3, 8] has numbers: {3, 4, 5, 6, 7, 8}
■ So the intersection is {3, 4, 5, 6} = [3, 6]
○ 1 15 20 30 ⇒ -1
"""

#Answer:
s1, e1, s2, e2 = map(int,input("Enter the entervals: ").split())
intersect_s = -1
intersect_e = -1

if s1 >= s2 and s1 <= e2:
    intersect_s = s1
elif e1 >= s2 and e1 <= e2:
    intersect_s = s2
else:
    intersect_s = -1
    intersect_e = -1

if e1 >= s2 and e1 <= e2:
    intersect_e = e1
else:
    intersect_e = e2

if intersect_s == -1 and intersect_e == -1:
    print(intersect_s)
else:
    print("Intersection [",intersect_s,",",intersect_e,"]")