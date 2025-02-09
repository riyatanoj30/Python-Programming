# Write menu driven python program to implement atleast 5 built-in functions of tuple
my_tuple = (10, 20, 30, 40, 50, 20, 60, 20)
while True:
    print("\n1. Display Tuple\n2. Length\n3. Count Element\n4. Find Index\n5. Convert to List\n6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Tuple:", my_tuple)
    elif choice == 2:
        print("Length:", len(my_tuple))
    elif choice == 3:
        x = int(input("Enter element: "))
        print(f"Count of {x}:", my_tuple.count(x))
    elif choice == 4:
        x = int(input("Enter element: "))
        print(f"Index of {x}:", my_tuple.index(x) if x in my_tuple else "Not found")
    elif choice == 5:
        print("Converted List:", list(my_tuple))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
