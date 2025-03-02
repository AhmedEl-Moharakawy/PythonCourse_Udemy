#Q:
"""
Is even? Print digits
● Read an integer N, then do the following
○ If the number is even: print the last digit of it
○ If the number is odd: do the following:
■ If number < 1000, print last 2 digits
■ If number >= 1000 and number < 1000000, print last 4 digits
■ Otherwise, print its negative value
● Stop the video and think: 1) Code 2) Good tests
● Testing examples of good coverage:
○ 234 ⇒ 4
○ 157 ⇒ 57
○ 567169 ⇒ 7169
○ 1000001 ⇒ -1000001
"""

#Answer:
num = int(input("Enter the number: "))

if num%2 == 0:
    #even
    print(num%10)
else:
    #odd
    if num < 1000:
        print(num%100)
    elif num < 1000000:
        print(num%1000)
    else:
        print(-1*num)