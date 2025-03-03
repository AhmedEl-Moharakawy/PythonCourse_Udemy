#Q: Print face down left angled triangle

"""
● Read integer N.
● Print a face down left angled triangle that has N rows as in picture

*****
****
***
**
*

"""

#Answer:
n = int(input("Enter numer of rows: "))

i = n
j = 0

while i > 0:
    while j < i:
        print("*",end='')
        j += 1
    print()
    i -= 1
    j = 0
