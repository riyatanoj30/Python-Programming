def print_star_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars
        print("*" * i)
n = 5
print_star_pattern(n)
