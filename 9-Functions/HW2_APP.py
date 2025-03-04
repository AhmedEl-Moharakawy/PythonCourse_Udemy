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

Rewrite the previous code as functions
● Print_menu: print the menu and read
a valid choice
○ Don’t return unless go number from 1 to 3
● Divide is just divide logic for handling
/ 0
○ If / 0 or // 0 return None
● Expression to parse e.g. x + y
● Interface: the core logic
○ Print, if else on choices
● Got lost? Just do your own rewriting
"""

#Answer:

def print_menu():
    print(""">> Menu:
        ○ Enter 1 to sum integers from 1 to N
        ○ Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
        ○ Enter 3 to end the program""")

def sum_1_to_n():
    sum = 0
    N = int(input("Enter N: "))
    if N < 0:
        print("Invalid Number!!")
        return 0
    else:
        while N > 0:
            sum += N
            N -= 1
        print("Total Sum =",sum)
        return 1

def divide(num1,num2,operation):
    if operation == '/':
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


def expression():
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
    elif operation == '/' or operation == '//':
        divide(num1,num2,operation)
    else:
        print("Invalid Operation!!")

def calculator_interface():
    print_menu()
    while True:
        choice = int(input("Select your operation: "))

        if choice == 1:
            if not sum_1_to_n():
                continue
        elif choice == 2:
            expression()
        elif choice == 3:
            print("End...")
            break
        else:
            print("Invalid Selection, Try Again!!")
            continue
    

calculator_interface()