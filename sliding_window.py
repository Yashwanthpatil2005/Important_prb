# Sliding Window Maximum

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

result = []

for i in range(len(arr) - k + 1):
    window = arr[i:i + k]
    result.append(max(window))

print("Maximum elements:", result)
