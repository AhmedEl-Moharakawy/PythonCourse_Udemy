#Q:
"""
● Write a program that read 3 strings.
○ For simplicity let’s say input is 3 letters A, B and C
● The output is A’B”C repeated 10 times
○ A’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”C
● Input:
○ I
○ am
○ Mostafa
● Output:
○ I'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'a
m"MostafaI'am"MostafaI'am"Mostafa
"""

#Answer:
str1=input("Enter String 1: ")
str2=input("Enter String 2: ")
str3=input("Enter String 3: ")

comp_str = str1 + "'" + str2 + '"' + str3

print(comp_str * 10)