"""
Print Fibonacci series up to n numbers.
"""
def fibonacci_series(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    print(f"Fibonacci series up to {n} numbers:")
    for term in fib_sequence:
        print(term, end=" ")

num_terms = int(input("Enter the number of Fibonacci terms to display: "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
   fibonacci_series(num_terms)
