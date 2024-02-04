'''Power Using a Recursive Function'''
def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * calculate_power(base, exponent - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = calculate_power(base, exponent)
print(f"{base}^{exponent} is: {result}")

