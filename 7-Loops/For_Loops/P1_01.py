#Q: Special Sum Homework

"""
● Read T for number of test cases.
● For each test case read integer N.
● Then read N integers a, b, c, ….. On seperate lines
● Compute the sum of:
○ (a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……)
○ That is the k-th number is repeated k times
● Expantation:
○ 2 test cases
○ 3 5 7 2
■ (5 + 7*7 + 2*2*2) = 62
○ 4 1 2 3 4
■ (1+2*2+3*3*3+4*4*4*4) = 288
"""

#Answer:

numOfTC = int(input("Enter the number of test cases: "))
pow = 1
pow_sum = 0

for i in range(numOfTC):
    numOfNumbers = int(input("Enter the number of numbers: "))
    for j in range(1,numOfNumbers+1):
        number = int(input("Enter the number: "))
        for k in range(j):
            pow *= number
        
        pow_sum += pow
        pow = 1
    print("Sum =",pow_sum)
    print("-"*20)
    pow_sum = 0