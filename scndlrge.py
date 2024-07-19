def find_scnd_largest(lst):
    if len(lst) < 2:
        return "List contain at least two elements"
    first = second = float('-inf')
    for number in lst:
        if number > first:
            second = first
            first = number
        elif number > second and number != first:
            second = number    
    if second == float('-inf'):
        return "No second largest element found"
    return second
print("Second largest element:", find_scnd_largest(my_list))
