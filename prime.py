# Prime Number Finder

num = int(input("Enter a number: "))

# Check if number is greater than 1
if num > 1:

    is_prime = True

    # Check factors
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Display result
    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")

else:
    print(num, "is NOT a Prime Number")