import random

def print_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    print_welcome_message()
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        user_guess = get_user_guess()

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
