# Problem 10: Remove duplicates from a list
# Find and fix the error

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"Without duplicates: {unique_numbers}")

