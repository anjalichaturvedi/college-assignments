'''Check if number is even or odd'''
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"The number is {result}.")
