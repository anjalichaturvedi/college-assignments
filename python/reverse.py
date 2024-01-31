"""
Input a 4-digit number and display the reversed number.
"""
def reverse_number():
    while True:
            number = int(input("Enter a 4-digit number: "))
            if 1000 <= number <= 9999:
                reversed_number = int(str(number)[::-1])
                print(f"Reversed number: {reversed_number}")
                break
            else:
                print("Please enter a valid 4-digit number.")

reverse_number()
