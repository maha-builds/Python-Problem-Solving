numbers = [12, 5, 8, 20, 3, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
