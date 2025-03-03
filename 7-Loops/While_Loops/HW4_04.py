#Q: Special Sum
"""
● Read integer T for number of test cases.
● For each test case read integer N.
● Then read N integers a, b, c, ….. On seperate lines
● Compute the sum of:
○ (a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……)
○ That is the k-th number is repeated k times
○ Don’t use the power operator (**)
● Expantation:
○ 2 test cases
○ 3 5 7 2
■ (5 + 7*7 + 2*2*2) = 62
○ 4 1 2 3 4
■ (1+2*2+3*3*3+4*4*4*4) = 288
"""

#Answer:
numOfTC = int(input("Enter number of Test Cases: "))
i,j,k = 0,0,0
sum = 0
pow_res = 1

while i < numOfTC:
    numOfNumbers = int(input("Enter number of numbers: "))
    while j < numOfNumbers:
        num = int(input("Enter a number: "))
        while k <= j:
            pow_res *= num
            k += 1
        sum += pow_res
        j += 1
        k = 0
        pow_res = 1
    print("Sum =",sum)
    print("-"*20)
    i += 1
    j = 0
    sum = 0
