# enter the week day from the user based on that display the day of the week on words
# Input the weekday number from the user
day_num = int(input("Enter a weekday number (1 for Monday, 2 for Tuesday, ..., 7 for Sunday): "))

# Check if the number is within the valid range
if 1 <= day_num <= 7:
    # Create a list of weekdays
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Display the corresponding day
    print(f"The day of the week is: {weekdays[day_num - 1]}")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
