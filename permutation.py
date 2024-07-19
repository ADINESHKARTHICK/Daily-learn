import itertools
def get_permutations(nums):
    perms = itertools.permutations(nums)
    return [list(perm) for perm in perms]
if __name__ == "__main__":
    user_input = input("Enter distinct integers separated by spaces: ")
    nums = list(map(int, user_input.split()))
    permutations = get_permutations(nums)
    print("All possible permutations:")
    for perm in permutations:
        print(perm)
