# Quick Sort in Python

def quick_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Select pivot element
    pivot = arr[len(arr) // 2]

    # Elements smaller than pivot
    left = [x for x in arr if x < pivot]

    # Elements equal to pivot
    middle = [x for x in arr if x == pivot]

    # Elements greater than pivot
    right = [x for x in arr if x > pivot]

    # Recursive sorting
    return quick_sort(left) + middle + quick_sort(right)


# Input array
arr = [10, 7, 8, 9, 1, 5]

print("Original Array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted Array:", sorted_arr)