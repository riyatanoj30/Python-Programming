def print_number_pattern(n):
    num = 1  # Start the number from 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
n = 5
print_number_pattern(n)
