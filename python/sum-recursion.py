'''Find sum to n using recursion'''
def sum_of_first_n_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_first_n_numbers(n - 1)

num = int(input("Enter a number: "))
result = sum_of_first_n_numbers(num)
print(f"The sum of first {num} numbers is: {result}")
