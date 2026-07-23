# Move All Zeros to the End

arr = [0, 1, 0, 3, 12]

position = 0

# Move non-zero elements to the front
for i in range(len(arr)):
    if arr[i] != 0:
        arr[position], arr[i] = arr[i], arr[position]
        position += 1

print("Array after moving zeros:", arr)
