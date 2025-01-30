# enter the number from a user the number should be between 0 - 9 based on the number entered display it in words
# Input a number from the user
num = int(input("Enter a number between 0 and 9: "))

# Check if the number is within the valid range
if 0 <= num <= 9:
    # Create a list of words for numbers 0-9
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # Display the corresponding word
    print(f"The number {num} in words is: {words[num]}")
else:
    print("Invalid input. Please enter a number between 0 and 9.")
