# Menu-driven calculator program
while True:
    # Displaying the menu
    print("\nMenu:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Floor Division (//)")
    print("6. Exponentiation (**)")
    print("7. Modulus (%)")
    print("8. Exit")
    
    # Taking the user's choice
    choice = input("Enter the operation number: ")

    # Exit condition
    if choice == '8':
        print("Exiting the program. Goodbye!")
        break

    # Taking input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation based on user's choice
    if choice == '1':
        print(f"The result is: {num1 + num2}")
    elif choice == '2':
        print(f"The result is: {num1 - num2}")
    elif choice == '3':
        print(f"The result is: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error! Division by zero.")
    elif choice == '5':
        if num2 != 0:
            print(f"The result is: {num1 // num2}")
        else:
            print("Error! Division by zero.")
    elif choice == '6':
        print(f"The result is: {num1 ** num2}")
    elif choice == '7':
        print(f"The result is: {num1 % num2}")
    else:
        print("Invalid choice! Please select a valid operation.")
