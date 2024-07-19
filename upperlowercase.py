def convert_case(s):
    upper = s.upper()
    lower = s.lower()
    return upper, lower
input_string = "Hello, World!"
upper_string, lower_string = convert_case(input_string)
print(f"Original String: {input_string}")
print(f"Uppercase String: {upper_string}")
print(f"Lowercase String: {lower_string}")
