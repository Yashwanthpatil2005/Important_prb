# Count Occurrences of a Given Number

arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter the number to count: "))

count = 0

for num in arr:
    if num == target:
        count += 1

print("Number of occurrences:", count)
