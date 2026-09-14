numbers = [12, 45, 7, 89, 23]

larger = numbers[0]
second_large = numbers[0]

for num in numbers:
    if num > larger:
        second_large = larger
        larger = num
    elif num > second_large and num != larger:
        second_large = num

print(second_large)
print(larger)
