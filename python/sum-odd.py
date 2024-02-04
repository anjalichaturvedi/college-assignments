'''Sum of odd numbers to 0 to n'''
def sum_of_odd_numbers(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

num = int(input("Enter a number: "))
result = sum_of_odd_numbers(num)
print(f"The sum of odd numbers between 1 to {num} is: {result}")
