#Q: Repeat Me
"""
● Read integer N and string S.
● Print S repeated N times as below
● Input: 5 Hi
● Output: HiHiHiHiHi
● Note: we can use string * 5
○ Please use while loops
"""

#Answer:
num, sentence = input("Enter Number of repeated times and the string: ").split()
num = int(num)
i = 0
while i < num:
    print(sentence,end="")
    i += 1
