#Q:Numbers divisible by 3
"""
● Read an integer X
● Print all numbers that are divisible by 3 from 1 to X.
○ These are 3, 6, 9, 12, 15, 18, ….. (multiple of 3)
● See example for input 12
● Stop the video and think first
"""

#Answer:
num = int(input("Enter a number: "))
div = 3 #as assumed from 1

if num < 3:
    print("Invalid! Number is less than 3")
else:
    while div <= num:
        print(div)
        div += 3
