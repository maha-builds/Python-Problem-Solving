list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 80]

new_list = []

for num in list1:
    if num in list2:
        new_list.append(num)

print(new_list)
