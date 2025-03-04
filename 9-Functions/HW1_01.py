#Q: Special Multiplication
"""
● Develop function: def special_multiplication(string):
● It returns a string where each character is repeated according to its position
○ Input: abcxf
○ Output: abbcccxxxxfffff
○ Observe
■ a repeated once
■ b twice
■ c 3 times
■ x 4 times
■ And so on
"""

#Answer:

def special_multiplication(input_string):
    output_string = ''
    for count, i in enumerate(input_string):
        output_string += i * (count+1)
        count += 1

    return output_string

print(special_multiplication("Ahmed"))