#Write menu driven python program to implement atleast 5 built-in functions of dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
while True:
    print("\n1. Display\n2. Add/Update\n3. Remove\n4. Show Keys\n5. Show Values\n6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Dictionary:", my_dict)
    elif choice == 2:
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
    elif choice == 3:
        key = input("Enter key to remove: ")
        my_dict.pop(key, "Key not found")
    elif choice == 4:
        print("Keys:", my_dict.keys())
    elif choice == 5:
        print("Values:", my_dict.values())
    elif choice == 6:
        break
    else:
        print("Invalid choice!")
