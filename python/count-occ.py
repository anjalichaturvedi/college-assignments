numbers = [1, 3, 2, 4, 1, 2, 3, 5, 6, 4, 5, 6, 3, 2, 3, 1, 2, 3, 4, 5]

for num in range(1, 7):
    count = numbers.count(num)
    print(f"{num} occurs {count} number of times")
