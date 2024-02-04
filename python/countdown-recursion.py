'''Countdown from a given number to 0'''
def countdown(n):
    if n < 0:
        return
    else:
        print(n)
        countdown(n - 1)

num = int(input("Enter a number for countdown: "))
print(f"\nCountdown from {num} to 0:")
countdown(num)
