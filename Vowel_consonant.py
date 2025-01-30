# check weather the character is vowel or consonant
# Input a character from the user
char = input("Enter a character: ").lower()

# Check if the character is a vowel or consonant
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.") # to embed expressions directly inside a sting
else:
    print("Invalid input. Please enter a valid alphabetic character.")
