#Q:Print Diamond

"""
● Read an integer N. Print diamond of 2N rows as below.
   *
  ***
 *****
*******
*******
 *****
  ***
   *
"""

#Answer:

n = int(input("Enter number of rows: "))
i = 0 
j = 0

while i < n:
    while j <= 2*n-1:
        if j >= n-i-1 and j <= n+i-1:
            print("*",end='')
        else:
            print(' ',end='')
        j += 1
    print()
    i += 1
    j = 0

i = 0

while i < n:
    while j <= 2*n-1:
        if j >= i and j < 2*n-i-1:
            print("*",end='')
        else:
            print(' ',end='')
        j += 1
    print()
    i += 1
    j = 0
