# Intersection of Two Arrays

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

intersection = []

for num in arr1:
    if num in arr2 and num not in intersection:
        intersection.append(num)

print("Intersection:", intersection)
