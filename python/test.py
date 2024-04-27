import sqlite3

conn = sqlite3.connect('MyDB.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Subject (
                SubjectId INTEGER PRIMARY KEY,
                Name TEXT,
                MaxMarks INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Student (
                EnrollmentNumber INTEGER PRIMARY KEY,
                Name TEXT,
                Course TEXT)''')

subject_records = [(1, 'Math', 100),
                   (2, 'Science', 90),
                   (3, 'History', 80),
                   (4, 'English', 95)]

student_records = [(101, 'Alice', 'Engineering'),
                   (102, 'Bob', 'Computer Science'),
                   (103, 'Charlie', 'Physics'),
                   (104, 'David', 'Mathematics')]

cursor.executemany('''INSERT INTO Subject (SubjectId, Name, MaxMarks) 
                   VALUES (?, ?, ?)''', subject_records)

cursor.executemany('''INSERT INTO Student (EnrollmentNumber, Name, Course) 
                   VALUES (?, ?, ?)''', student_records)

print("Subject table:")
cursor.execute("SELECT * FROM Subject")
print(cursor.fetchall())

print("Student table:")
cursor.execute("SELECT * FROM Student")
print(cursor.fetchall())

cursor.execute("SELECT EnrollmentNumber FROM Student")
print("Enrollment Numbers:", [record[0] for record in cursor.fetchall()])

conn.close()
