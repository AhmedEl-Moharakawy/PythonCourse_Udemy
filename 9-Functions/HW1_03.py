#Q: Get nth-prime
"""
● Implement the following 2 functions:
● is_prime(num);
○ Return true if number is prime (it is not divisible by any number > 1
● nth_prime(n);
○ Return the n-th prime number. It should use is_prime function
○ E.g nth_prime(6) = 13
■ Recall primes are: 2, 3, 5, 7, 11, 13, 17, 19
"""

#Answer:

def is_prime(num):
    for i in range(2,9):
        if (num % i == 0) and (num != i):
            return False
    return True


def nth_prime(n):
    count = 0
    i = 2
    while True:
        if is_prime(i):
            count += 1
            if count == n:
                return i
        
        i += 1
    
    return -1 #can't be reached


print(nth_prime(7))