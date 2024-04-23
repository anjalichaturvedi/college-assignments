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

# Add 2 extra marks to last subject
for result in result_sheet:
    result[-1] += 2

# Reprint result sheet
for result in result_sheet:
    print(f"Name: {result[0]}, Section: {result[1]}, Percentage: {result[2]}")
