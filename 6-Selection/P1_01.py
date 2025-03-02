#Q:
"""
● Given two numbers and a sign between them which will indicate if the user
want the addition, subtraction, float division or multiplication of these two
numbers, find the value of the answer.
○ Overall: + - * /
○ In case of division by zero: print NA
● Inputs ⇒ outputs
○ 7 + 55 ⇒ 62
○ 7 * 10 ⇒ 70
○ 5 / 0 ⇒ NA
"""

#Answer:
num1, operation, num2 = input("Enter equation with space separation: ").split()
num1 = float(num1)
num2 = float(num2)

if operation == '+':
    print(num1,"+",num2,"=",num1+num2)
elif operation == '-':
    print(num1,"-",num2,"=",num1-num2)
elif operation == '*':
    print(num1,"*",num2,"=",num1*num2)
elif operation == '/':
    if num2 == 0:
        print(num1,"/",num2,"=","NA")
    else:
        print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid operation")
