#                                           Task 3
# Password Generator

import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_special=True):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Sophisticated Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
                continue
            
            include_lowercase = input("Include lowercase letters? (yes/no): ").lower() in ['yes', 'y']
            include_uppercase = input("Include uppercase letters? (yes/no): ").lower() in ['yes', 'y']
            include_digits = input("Include digits? (yes/no): ").lower() in ['yes', 'y']
            include_special = input("Include special characters? (yes/no): ").lower() in ['yes', 'y']

            password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special)
            print("Generated Password:", password)
            break
        except ValueError as ve:
            print("Error:", ve)
        except KeyboardInterrupt:
            print("\nOperation interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()
