# Subarray Sum K

arr = [1, 2, 3, 4, 5]
k = 9

current_sum = 0
found = False

for i in range(len(arr)):
    current_sum = 0

    for j in range(i, len(arr)):
        current_sum += arr[j]

        if current_sum == k:
            print("Subarray found:", arr[i:j + 1])
            found = True
            break

    if found:
        break

if not found:
    print("Subarray not found")
