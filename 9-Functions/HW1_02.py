#Q:
"""
Max of 6 numbers
● Develop these 4 functions to help
compute maximum of 6 numbers
● Each function should be only a single
line of code
○ Hint: make use of the other functions
"""

#Answer:

def max2(a,b):
    if a > b:
        return a
    return b

def max3(a,b,c):
    return max2(a, max2(b,c))

def max4(a,b,c,d):
    return max2(a, max3(b,c,d))

def max5(a,b,c,d,e):
    return max2(a, max4(b,c,d,e))

def max6(a,b,c,d,e,f):
    return max2(a, max5(b,c,d,e,f))

print(max6(5,8,13,4,10,1))