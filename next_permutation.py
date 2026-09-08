# Next Permutation

arr = [1, 2, 3]

n = len(arr)

# Step 1: Find the first decreasing element from the right
i = n - 2

while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1

# Step 2: Find the element just greater than arr[i]
if i >= 0:
    j = n - 1

    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]

# Step 3: Reverse the elements after i
left = i + 1
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Next Permutation:", arr)
