# Write python program using built-in functions using factorial of a number
import math
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")
