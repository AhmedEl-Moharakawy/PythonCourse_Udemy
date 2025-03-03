#Q: Reverse number
"""
● Read an integer N, then find its reverse integer R
○ Print R R*3
● input ⇒ Output
○ 123 ⇒ 321 963
"""

#Answer:
num = int(input("Enter a number: "))

new_num = 0

while num > 0:
    rem = num % 10
    num //= 10
    new_num = new_num * 10 + rem

print("New Number =",new_num,", R*3=",new_num*3)

