set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = set1.intersection(set2)

print("Common elements:", common_elements)

for element in common_elements:
    freq_set1 = list(set1).count(element)
    freq_set2 = list(set2).count(element)
    print(f"{element}: Frequency in set1: {freq_set1}, Frequency in set2: {freq_set2}")
