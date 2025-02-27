#Q:
"""
Given 8 space-separated integers, find the sum of those in even places and
the sum of those in odd places.
○ Note: Even place means the 2nd, 4th, 6th or 8th numbers,
odd places are the 1st, 3rd, 5th and 7th numbers.
○ Note: the 8 numbers will be on the same line
○ Note: Don't print any welcome or by messages.
● Input: 11 2 7 9 12 -8 3 -1
● Output: 2 33
● Example Explanation:
○ 2 + 9 + (-8) + (-1) = 2 for the even places
○ 11 + 7 + 12 + 3 = 33 for the odd places
"""

#Answer:
n1,n2,n3,n4,n5,n6,n7,n8 = map(int, input().split())

print(n2+n4+n6+n8,n1+n3+n5+n7)