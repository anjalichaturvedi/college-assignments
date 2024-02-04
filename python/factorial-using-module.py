'''Factorial using recursion'''
import recursive_module

num = int(input("Enter a number: "))
result = recursive_module.calculate_factorial(num)
print(f"The factorial of {num} is: {result}")
