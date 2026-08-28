# Find Second Smallest Element

arr = [10, 20, 4, 45, 99]

smallest = arr[0]
second_smallest = arr[0]

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Smallest:", smallest)
print("Second Smallest:", second_smallest)
