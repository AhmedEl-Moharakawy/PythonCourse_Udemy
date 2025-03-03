#Q: Special Average
"""
● Read integer N, followed by reading N numbers
○ Each on separate lines
● Print 2 values
○ The average of the numbers in odd positions (1st, 3rd, 5th, …)
○ The average of the numbers in even positions (2nd, 4th, 6th, …)
● Explantation
○ (10+20+30)/3 = 20
○ (100+200+600)/3 = 300
"""

#Answer:
N = int(input("Enter number of the numbers: "))

sum_odd = 0
sum_even = 0
i = 1
odd_count = 0
even_count = 0
while i <= N:
    num = int(input("Enter a number: "))
    
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
        odd_count += 1
    
    i += 1

even_count = N - odd_count
odd_av = sum_odd / odd_count
even_av = sum_even / even_count
print("odds =",odd_av,",evens =",even_av)