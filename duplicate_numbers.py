numbers = [2, 5, 8, 2, 10, 5, 7, 8]
duplicate_numbers = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicate_numbers:
        duplicate_numbers.append(i)

print(duplicate_numbers)
