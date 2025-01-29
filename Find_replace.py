#3. consider the list with following [20,30,40,20,50] find and replace the first occurance of 20 with 10.
# Create the list
numbers = [20, 30, 40, 20, 50]

# Find and replace the first occurrence of 20 with 10
if 20 in numbers:
    index = numbers.index(20)  # Find the index of the first occurrence of 20
    numbers[index] = 10        # Replace it with 10

# Display the updated list
print(numbers)
