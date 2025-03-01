#Q: Is even?
"""
● The following code, reads an integer and computes a boolean if the number is
even in 3 different ways. The number can be +ve or -ve.
● Fill in the is_even to solve the problem in 3 ways as following
● Using only %2
● Using only %10
● Using only /2


num = int(input())

# Using only %2
is_even_1 = ???

# Using only /2
is_even_2 = ???

# Using only %10
is_even_3 = ???

print(is_even_1,is_even_2,is_even_3)
"""

#Answer:
num = int(input())

# Using only %2
is_even_1 = bool(not (num % 2))

# Using only /2
is_even_2 = bool(not(num / 2 - int(num / 2)))

# Using only %10
rem_10 = num % 10
is_even_3 = bool(rem_10 == 0 or rem_10 == 2 or rem_10 == 4 or rem_10 == 6 or rem_10 == 8)

print(is_even_1,is_even_2,is_even_3)