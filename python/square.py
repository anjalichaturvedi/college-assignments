'''Square of a number using function'''
def calculate_square(number):
    return number**2

# Input a number
num = int(input("Enter a number: "))
result = calculate_square(num)
print(f"The square of {num} is: {result}")
