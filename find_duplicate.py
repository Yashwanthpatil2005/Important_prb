# Find Duplicate Elements

arr = [1, 2, 3, 2, 4, 5, 3]

duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)
