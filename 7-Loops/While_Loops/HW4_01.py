#Q: Find NOs
"""
● Read integer N, then read N strings (one per line).
○ Print only the strings (of 2 letters).
○ These 2 letters must be letter ‘N’ and letter ‘O’ (regardless of
lower/upper case/order)
○ E.g. print “No”, “ON”, “no” but ignore e.g. “YEs”, “Noooo”
○ That is, the word of 2 letters only N and O
○ See the picture
"""

#Answer:
n = int(input("Enter the number of strings: "))
i = -1
while n > 0:
    string = input("Enter the string: ")
    if len(string) == 2:
        if string == "no" or string == "No" or string == "nO" or string == "NO" or string == "on" or string == "oN" or string == "On" or string == "ON":
            print("Match:", string)
            i = 0
            break
    
    n -= 1

if i == -1:
    print('No Match')