import custom_module

# Input a number
num = int(input("Enter a number: "))
if custom_module.is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
