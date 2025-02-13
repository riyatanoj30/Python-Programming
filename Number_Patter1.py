def print_number_pattern(n):
    for i in range(1, n + 1):
        # Print numbers from 1 to i
        print("".join(str(x) for x in range(1, i + 1)))
n = 5
print_number_pattern(n)
