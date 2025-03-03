#Q: Special multiples 2

"""
● Read an integer N (1 <= 30): Print the first N numbers that are
○ multiple of 3 but not multiple of 4
● Input: 11
● Output: 3 6 9 15 18 21 27 30 33 39 42
● Notice
○ 12 is divisible by both 3 and 4 ⇒ so excluded
"""

#Answer:
N = int(input("Enter N: "))
i = 1
count = 0
while count < N:
    if not(i % 3) and (i % 4):
        print(i)
        count += 1
 
    i += 1