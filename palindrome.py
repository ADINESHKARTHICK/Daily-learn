def is_palindrome(x):
    if x < 0:
        return False
      strx = str(x)
    return strx == str[::-1]
test_numbers = [121, -121, 10, 12321]
for num in test_numbers:
    result = is_palindrome(num)
    print(f"{num} is a palindrome: {result}")
