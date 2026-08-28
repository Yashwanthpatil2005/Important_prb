# Find Second Largest Element

arr = [10, 20, 4, 45, 99]

largest = arr[0]
second_largest = arr[0]

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)
