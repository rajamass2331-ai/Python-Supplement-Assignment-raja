# Problem 14: Check if a number is prime
# Find and fix the error

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"Is {num} prime? {is_prime(num)}")
