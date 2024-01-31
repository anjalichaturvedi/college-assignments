"""
Check whether a number is prime or not.
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

user_number = int(input("Enter a number: "))
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")