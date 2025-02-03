import random
import string

def generate_password(length=12):
    # Define possible characters for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure password length is at least 8 for security reasons
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Randomly select characters from the pool
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Automatic Password Generator!")
    
    # Get password length from user, default to 12 if not provided
    length = input("Enter the length of the password (minimum 8 characters, default is 12): ")
    length = int(length) if length else 12
    
    password = generate_password(length)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()