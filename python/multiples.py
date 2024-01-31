"""
Find the first 5 multiples of 6 using while loop and break.
"""
def find_multiples_of_six():
    multiples_count = 0
    num = 6
    while multiples_count < 5:
        print(num)
        multiples_count += 1
        num += 6

print("First 5 multiples of 6:")
find_multiples_of_six()