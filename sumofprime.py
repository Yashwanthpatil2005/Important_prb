# Sum of Two Prime Numbers with Validation

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if is_prime(num1) and is_prime(num2):

    total = num1 + num2

    print("Sum =", total)

else:
    print("One or both numbers are not prime numbers")