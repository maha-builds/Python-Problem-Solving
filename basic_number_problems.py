# Problem 1: Find the largest number

numbers = [12, 5, 8, 20, 3, 15, 7, 10]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# Problem 2: Find the smallest number

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
