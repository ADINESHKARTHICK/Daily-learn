numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"Unique elements: {list(unique_numbers)}")  # Convert back to list for printing
for num in numbers:
 if num not in unique_numbers:
unique_numbers.append(num)
print(f"Unique elements: {unique_numbers}")
