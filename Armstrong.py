# Write python program using built-in functions to check whether a number is Armstrong or not
num = int(input("Enter a number: "))
num_digits = len(str(num))
armstrong_sum = sum(int(digit) ** num_digits for digit in str(num))
if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
