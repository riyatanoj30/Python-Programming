# enter the month number from the user based on the number display the month
# Input the month number from the user
month_num = int(input("Enter a month number (1 for January, 2 for February, ..., 12 for December): "))

# Check if the number is within the valid range
if 1 <= month_num <= 12:
    # Create a list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # Display the corresponding month
    print(f"The month is: {months[month_num - 1]}")
else:
    print("Invalid input. Please enter a number between 1 and 12.")
