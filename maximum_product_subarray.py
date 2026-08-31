# Maximum Product Subarray

arr = [2, 3, -2, 4]

max_product = arr[0]
current_max = arr[0]
current_min = arr[0]

for i in range(1, len(arr)):

    num = arr[i]

    if num < 0:
        current_max, current_min = current_min, current_max

    current_max = max(num, current_max * num)
    current_min = min(num, current_min * num)

    max_product = max(max_product, current_max)

print("Maximum Product:", max_product)
