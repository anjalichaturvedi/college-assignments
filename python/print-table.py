"""
Print the table of the given number up to 10.
"""
def print_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Get user input for the number
user_number = int(input("Enter a number: "))

# Print the table using the function
print_table(user_number)
