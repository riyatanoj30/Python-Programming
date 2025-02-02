# Write python program to create a menu and implement various operations, built-in functions of dictionary
def main():
    my_dict = {}
    
    while True:
        print("\nMenu:")
        print("1. Add key-value")
        print("2. Show dictionary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print("Added.")
        
        elif choice == "2":
            print("Dictionary:", my_dict)
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()