#Q: Special Calculator
"""
● Design a small application that keeps asking the user 3 choices:
○ Enter 1 to sum integers from 1 to N
○ Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
■ Expect 3 items. Operations are: + - * / // **
○ Enter 3 to end the program
● The user should input value from 1 to 3
○ Otherwise, inform that this is invalid and try again
● Take proper input from the user and compute the answer
○ See next console simulation
"""

#Answer:

print(""">> Menu:
   ○ Enter 1 to sum integers from 1 to N
   ○ Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
   ○ Enter 3 to end the program""")

while True:
    choice = int(input("Select your operation: "))

    if choice == 1:
        sum = 0
        N = int(input("Enter N: "))
        if N < 0:
            print("Invalid Number!!")
            continue
        while N > 0:
            sum += N
            N -= 1
        print("Total Sum =",sum)
        
    elif choice == 2:
        num1, operation, num2 = input("Enter the expression: ").split()
        num1 = int(num1)
        num2 = int(num2)
        if operation == '+':
            print(num1,'+',num2,'=',num1 + num2)
        elif operation == '-':
            print(num1,'-',num2,'=',num1 - num2)
        elif operation == '*':
            print(num1,'*',num2,'=',num1 * num2)
        elif operation == '**':
            print(num1,'**',num2,'=',num1 ** num2)
        elif operation == '/':
            if num2 == 0:
                print("Invalid Operation!!")
            else:
                print(num1,'/',num2,'=',num1 / num2)
        elif operation == '//':
            if num2 == 0:
                print("Invalid Operation!!")
            else:
                print(num1,'//',num2,'=',num1 // num2)
        else:
            print("Invalid Operation!!")
    elif choice == 3:
        print("End...")
        break
    else:
        print("Invalid Selection, Try Again!!")
        continue