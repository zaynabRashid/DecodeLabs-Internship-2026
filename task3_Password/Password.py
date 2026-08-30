import random
import string


# -----------------------------------------
# Random Password Generator
# -----------------------------------------

print("========== Random Password Generator ==========")

# Ask the user for password length
try:
    password_length = int(input("Enter password length: "))

    if password_length < 8:
        print("Password length must be at least 8 characters.")

    else:
        characters = string.ascii_letters + string.digits + "@#$%^&*!?"

        password = ""

        for i in range(password_length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number.")