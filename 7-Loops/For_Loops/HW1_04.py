#Q: Is Prime?
"""
● Read an integer N (< 500) and print YES if it is prime, otherwise NO
○ A prime number is greater than 1 AND cannot be formed by multiplying two smaller numbers.
■ In other words, number%whatever != 0
■ The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29.
● Input ⇒ Output
○ 13 ⇒ YES (only 1 * 13)
○ 12 ⇒ NO (E.g. 12 = 2 *6, so 12 can be divided by 2 or 6)
"""

#Answer:
num = int(input("Enter your number: "))
is_prime = 0

if num > 500 or num < 0:
    print("Invalid Number !!")
else:
    for i in range(2,10,1):
        if num % i == 0 and num != i:
            is_prime = 1
            break
    
    if is_prime:
        print("No")
    else:
        print("yes")
