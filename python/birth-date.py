"""
Print the names of students except those born in July.
"""

def print_students_except_july(students_data):
    for name, birth_month in students_data.items():
        if birth_month == 7:
            continue
        print(name)

students_data = {}

for i in range(1, 11):
    name = input(f"Enter the name of student {i}: ")
    birth_month = int(input(f"Enter the birth month of {name} (in numeral form): "))
    students_data[name] = birth_month

print("Names of students born in months other than July:")
print_students_except_july(students_data)
