numbers = [10, 25, 7, 40, 18]

large_number = numbers[0]
second_large = numbers[0]

for num in numbers:
    if num > large_number:
        second_large = large_number
        large_number = num
    elif num > second_large and num != large_number:
        second_large = num

print(second_large)
