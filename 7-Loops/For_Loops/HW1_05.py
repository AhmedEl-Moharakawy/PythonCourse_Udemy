#Q: Print Primes
"""
● Read integer N (<500), then print all prime numbers <= N
● Input ⇒ Output
○ 18 ⇒ 2 3 5 7 11 13 17
"""

#Answer:
n = int(input("Enter your number: "))
is_prime = 0

if n > 500 or n < 2:
    print("Invalid Number !!")
else:
    for i in range(2,n+1):
        for j in range(2,10,1):
            if i % j == 0 and i != j:
                is_prime = 1
        if not is_prime:
            print(i,end=' ')
        is_prime = 0

