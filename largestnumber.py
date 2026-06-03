# Find Largest Element from User Input

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is:", largest)