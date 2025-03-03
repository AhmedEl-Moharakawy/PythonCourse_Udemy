#Q: Special multiples 1

"""
● Read an integer N : print all numbers <= N that satisfy the following property
○ Either number is divisible by 8
○ Or divisible by both 4 and 3
● Input: 100
● Output: 0 8 12 16 24 32 36 40 48 56 60 64 72 80 84 88 96
"""

#Answer:
N = int(input("Enter N: "))
temp = 0

while temp <= N:
    if not(temp % 8) or (not(temp % 3)and not(temp % 4)):
        print(temp)
    
    temp += 1