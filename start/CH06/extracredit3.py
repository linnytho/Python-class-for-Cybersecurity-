import string
import secrets

# Color codes for terminal output
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"


# Get a yes/no answer from the user
def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").lower().strip()

        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        else:
            print("Please enter y or n.")


# Get a number within a specified range
def get_number(question, minimum, maximum):
    while True:
        try:
            number = int(input(question))

            if minimum <= number <= maximum:
                return number

            print(f"Please enter a number from {minimum} to {maximum}.")

        except ValueError:
            print("Please enter a valid number.")


# Generate a password
def generate_password(length, groups, first_letter):

    # Combine all available characters
    all_characters = "".join(groups.values())

    # Create a separate pool for the first letter
    letters = string.ascii_letters

    if first_letter:
        if not letters:
            raise ValueError("No letters available.")

    # Make sure the password has enough space
    required = list(groups.values())

    if length < len(required) + int(first_letter):
        raise ValueError("Password length is too short for selected options.")

    # Choose at least one character from each selected group
    password_characters = []

    for group in required:
        password_characters.append(secrets.choice(group))

    # Choose the first character if requested
    if first_letter:
        first_character = secrets.choice(letters)
    else:
        first_character = ""

    # Fill the remaining positions
    remaining_length = length - len(password_characters) - int(first_letter)

    for _ in range(remaining_length):
        password_characters.append(secrets.choice(all_characters))

    # Shuffle the remaining characters
    secrets.SystemRandom().shuffle(password_characters)

    return first_character + "".join(password_characters)


# Display password with colored characters
def display_password(password):

    for character in password:

        if character.isalpha():
            print(GREEN + character + RESET, end="")

        elif character.isdigit():
            print(BLUE + character + RESET, end="")

        else:
            print(YELLOW + character + RESET, end="")

    print()


# Main program
def main():


    # Ask for password length
    length = get_number(
        "Enter password length (4-300): ", 4, 300
    )

    # Select character types
    groups = {}

    if ask_yes_no("Include lowercase letters?"):
        groups["lowercase"] = string.ascii_lowercase

    if ask_yes_no("Include uppercase letters?"):
        groups["uppercase"] = string.ascii_uppercase

    if ask_yes_no("Include numbers?"):
        groups["numbers"] = string.digits

    if ask_yes_no("Include symbols?"):
        groups["symbols"] = string.punctuation

    # Optional Unicode characters
    if ask_yes_no("Include custom Unicode characters?"):
        print("Paste the Unicode characters you want to include.")
        print("On Mac, use Control + Command + Space to open Character Viewer.")

        unicode_characters = input("Enter Unicode characters: ")

        if unicode_characters:
            groups["unicode"] = unicode_characters

    # Check that at least one character group is selected
    if not groups:
        print("Please select at least one character type.")
        return

    # Exclude similar characters
    if ask_yes_no("Exclude similar characters (i, l, 1, L, I, O, 0)?"):

        similar = "il1Lo0O"

        for group in groups:
            groups[group] = "".join(
                character for character in groups[group]
                if character not in similar
            )

    # Exclude ambiguous characters
    if ask_yes_no("Exclude ambiguous characters?"):

        ambiguous = "{}[]()/\\'\"~,;:.<>|"

        for group in groups:
            groups[group] = "".join(
                character for character in groups[group]
                if character not in ambiguous
            )

    # Check that no selected group became empty
    if any(not characters for characters in groups.values()):
        print("One of your selected character groups is empty.")
        return

    # First character must be a letter
    first_letter = ask_yes_no(
        "Should the first character be a letter?"
    )

    # Number of passwords to generate
    quantity = get_number(
        "How many passwords do you want? (1-20): ", 1, 20
    )

    # Generate passwords

    try:
        for number in range(1, quantity + 1):

            password = generate_password(
                length, groups, first_letter
            )

            print(f"\nPassword {number}: ", end="")
            display_password(password)

    except ValueError as error:
        print("Error:", error)


# Run the program
if __name__ == "__main__":
    main()
