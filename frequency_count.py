numbers = [2, 3, 2, 5, 3, 2, 7, 3, 3]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print(frequency)
