students_dict = {}
num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    rollno = input("Enter roll number: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    students_dict[rollno] = {'name': name, 'age': age, 'grade': grade}

rollno = input("Enter roll number to display information: ")
if rollno in students_dict:
    student_info = students_dict[rollno]
    print(f"Name: {student_info['name']}, Age: {student_info['age']}, Grade: {student_info['grade']}")
else:
    print("Student not found in the dictionary.")

rollno = input("Enter roll number to update information: ")
if rollno in students_dict:
    print("What would you like to update?")
    print("1. Name\n2. Age\n3. Grade\n4. Remove student and insert new rollno")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_name = input("Enter new name: ")
        students_dict[rollno]['name'] = new_name
    elif choice == 2:
        new_age = int(input("Enter new age: "))
        students_dict[rollno]['age'] = new_age
    elif choice == 3:
        new_grade = input("Enter new grade: ")
        students_dict[rollno]['grade'] = new_grade
    elif choice == 4:
        new_rollno = input("Enter new roll number: ")
        students_dict[new_rollno] = students_dict.pop(rollno)
else:
    print("Student not found in the dictionary.")
