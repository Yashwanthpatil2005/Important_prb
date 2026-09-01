# Missing and Repeating Number

arr = [1, 2, 2, 4, 5]

n = len(arr)

for i in range(1, n + 1):
    count = arr.count(i)

    if count == 0:
        missing = i

    elif count > 1:
        repeating = i

print("Missing Number:", missing)
print("Repeating Number:", repeating)
