# Left Rotate Array by K Positions

arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)

rotated = arr[k:] + arr[:k]

print("Rotated Array:", rotated)
