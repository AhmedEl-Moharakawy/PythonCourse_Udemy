#Q: Digits sum in range
"""
● Read three integers N, A, B.
● Print the summation of the numbers between 1 and N whose sum of digits is
between A and B.
● Input ⇒ Output
○ 20 2 5 ⇒ 84
■ Numbers whose sums of digits are between 2 and 5, are: 2,3,4,5,11,12,13,14, 20.
● E.g. digits sum of 13 is 4 : which is between (2, 5)
○ 10 1 2 ⇒ 13
○ 100 4 16 ⇒ 4554
"""

#Answer:
N,A,B = map(int,input("Enter N, A, B: ").split())
dig_sum = 0
total_sum = 0

for i in range(1,N+1):
    #get digits sum
    num = i
    while num > 0:
        dig_sum += (num % 10)
        num //= 10 

    if dig_sum >= A and dig_sum <= B:
        total_sum += i
    
    dig_sum = 0

print("Sum =",total_sum)
