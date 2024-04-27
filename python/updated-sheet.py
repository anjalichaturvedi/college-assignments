students = [
    ("John Doe", "A", 85, 90, 78),
    ("Jane Smith", "B", 75, 80, 82),
    ("Michael Johnson", "A", 92, 88, 95)
]

result_sheet = []
for student in students:
    name = student[0]
    section = student[1]
    marks = student[2:]
    percentage = sum(marks) / len(marks)
    result_sheet.append((name, section, percentage))

result_sheet_list = [list(student) for student in result_sheet]

for student in result_sheet_list:
    del student[2]

for student in result_sheet_list:
    print(f"Name: {student[0]}, Section: {student[1]}, Percentage: {student[2]}")
