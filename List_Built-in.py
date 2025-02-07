# Write menu driven python program to implement atleast 5 built-in functions of list
my_List = (10, 20, 30, 40, 50, 20, 60, 20)
while True:
    print("\n1. Display List\n2. Length\n3. Count Element\n4. Find Index\n5. Convert to Tuple\n6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("List:", my_List)
    elif choice == 2:
        print("Length:", len(my_List))
    elif choice == 3:
        x = int(input("Enter element: "))
        print(f"Count of {x}:", my_List.count(x))
    elif choice == 4:
        x = int(input("Enter element: "))
        print(f"Index of {x}:", my_List.index(x) if x in my_List else "Not found")
    elif choice == 5:
        print("Converted List:", list(my_List))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")