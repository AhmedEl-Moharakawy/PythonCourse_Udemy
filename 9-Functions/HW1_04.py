#Q: Get nth-fibonacci
"""
● Fibonacci is a popular sequence: 0, 1, 1, 2, 3, 5, 8, 13,
21, …
○ Every number is sum of last 2 numbers
○ E.g. 13 = 5 + 8
● Write function: nth_fib(n)
○ That returns the nth term
○ Hint: Simple loop
"""

#Answer:

def nth_fib(n):
    tail = 0
    head = 1
    
    print(tail,end=' ')
    print(head,end=' ')
    
    for i in range(n):
        next_num = tail + head
        print(next_num,end=' ')
        tail = head
        head = next_num

nth_fib(15)