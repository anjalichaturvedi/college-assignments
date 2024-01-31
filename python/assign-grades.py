"""
Assign grades based on marks and print the result.
"""
def assign_grades(student_data):
    for name, marks in student_data.items():
        if marks >= 90:
            grade = 'A'
        elif 75 <= marks <= 89:
            grade = 'B'
        elif 60 <= marks <= 74:
            grade = 'C'
        elif 45 <= marks <= 59:
            grade = 'D'
        else:
            grade = 'E'
        print(f"{name}: Marks = {marks}, Grade = {grade}")

students_data = {}
for i in range(1, 11):
    name = input(f"Enter the name of student {i}: ")
    marks = int(input(f"Enter the marks of {name}: "))
    students_data[name] = marks

print("Grades for students:")
assign_grades(students_data)
