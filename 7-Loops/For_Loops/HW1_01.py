#Q: Printing X
"""
● Read an Integer N, then print an X using * as following
○ N always odd
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
"""

#Answer:
n = int(input("Enter number of rows: "))

if n % 2 == 0 or n < 0:
    print("Invalid number of rows!!")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j == i or j == n - i + 1:
                print("*",end = '')
            else:
                print(" ",end = '')
        print()
