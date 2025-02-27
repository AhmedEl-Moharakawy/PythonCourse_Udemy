#Q: Write a program that reads 2 students information about math exam
"""
○ For each student read: his name, id and grade
● Print the students
● Print the grades average
● See the picture
"""

#Answer:
St1_name = input("Enter the first student's name: ")
St1_ID = input("Enter the first student's ID: ")
St1_grade = input("Enter the first student's grade: ")

St2_name = input("Enter the second student's name: ")
St2_ID = input("Enter the second student's ID: ")
St2_grade = input("Enter the second student's grade: ")

print("Information for students and their \"math\" grades")
print(St1_name+"("+ St1_ID +")", "got grade:", float(St1_grade))
print(St2_name+"("+ St2_ID +")", "got grade:", float(St2_grade))
print("Average math grade is", (float(St1_grade) + float(St2_grade))/2)