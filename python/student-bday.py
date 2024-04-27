students_birthday = {}
while True:
    name = input("Enter name: ")
    month = int(input("Enter birthday month (1-12): "))
    if 1 <= month <= 12:
        students_birthday[name] = month
    else:
        print("Invalid month. Please enter a month between 1 and 12.")
    
    more = input("Enter 'yes' to add more students or any other key to stop: ")
    if more.lower() != 'yes':
        break

for name, month in students_birthday.items():
    if month != 2:
        print(f"{name}, you were born in month {month}.")
