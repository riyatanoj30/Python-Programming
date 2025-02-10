# Write python program using built-in functions to check whether a number is perfect or not
num = int(input("Enter a number: "))
divisor_sum = sum(i for i in range(1, num) if num % i == 0)
if num == divisor_sum:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
