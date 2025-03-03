#Q: Print left angled triangle
"""
● Given an integer N. Print a left angled
triangle that has N rows.
● See picture for IO

*
**
***
****
*****

"""

#Answer:
n = int(input("Enter numer of rows: "))

i = 0
j = 0

while i < n:
    while j < i + 1:
        print("*",end="")
        j += 1
    
    print("\n",end="")
    i += 1
    j = 0