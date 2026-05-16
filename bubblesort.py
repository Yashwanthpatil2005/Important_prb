# Bubble Sort in Python

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Traverse through all array elements
        for j in range(0, n - i - 1):

            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example list
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Before Sorting:")
print(numbers)

bubble_sort(numbers)

print("After Sorting:")
print(numbers)