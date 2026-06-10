# Move All Zeros to the End

arr = [0, 1, 0, 3, 12]

result = []

# Add non-zero elements
for num in arr:
    if num != 0:
        result.append(num)

# Count zeros
zero_count = len(arr) - len(result)

# Add zeros at the end
result.extend([0] * zero_count)

print("Original Array:", arr)
print("Modified Array:", result)
