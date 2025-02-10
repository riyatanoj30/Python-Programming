# Write python program using built-in functions to display fibonache series
num_terms = int(input("Enter the number of terms: "))
a, b = 0, 1
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    for _ in range(num_terms):
        print(a, end=" ")
        a, b = b, a + b