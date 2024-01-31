"""
Print odd numbers from 1 to 10 using continue.
"""
def print_odd_numbers():
    for num in range(1, 11):
        if num % 2 == 0:
            continue
        print(num)

print("Odd numbers from 1 to 10:")
print_odd_numbers()
