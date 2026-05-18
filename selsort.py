# Selection Sort in Python

def selection_sort(arr):

    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Assume current index is minimum
        min_index = i

        # Find the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Input array
arr = [64, 25, 12, 22, 11]

print("Original Array:", arr)

selection_sort(arr)

print("Sorted Array:", arr)