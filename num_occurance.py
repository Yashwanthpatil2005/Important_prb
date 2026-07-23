# Count Occurrences of a Given Number

arr = [1, 2, 3, 2, 4, 2, 5]
target = 2

count = 0

for num in arr:
    if num == target:
        count += 1

print("Number of occurrences:", count)
