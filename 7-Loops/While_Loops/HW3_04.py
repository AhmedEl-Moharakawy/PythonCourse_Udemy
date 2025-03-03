#Q: Minimum of values

"""
● Read T for number of test cases.
● For each test case read integer N: For number of
integers to read
● Then read N integers, each on a seperate line
● For each test case, print the minimum of the N
integers.
● See picture
○ 2 for 2 test cases
■ The length of the first is 6
■ And the length of the second is 3
"""

#Answer:
numOfTests = int(input("Enter the number of test cases: "))
i = 0

while i < numOfTests:
    N = int(input("Enter the number of numbers: "))
    j = 0
    number = int(input("Enter the number: "))
    min = number

    while j < N - 1:
        number = int(input("Enter the number: "))
        if number < min:
            min = number
        j += 1
    
    print("The min =",min)
    i += 1
    print("-"*20)
