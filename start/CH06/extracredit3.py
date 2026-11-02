import string 
import secrets 

#color codes for terminal output 
GREEN="\033[92m"
BLUE="\033[94m"
YELLOW="\033[93m"
RESET="\033[0m"

# get a yes/no answer from the user 
def ask_yes_no(question):
    while True: 
        answer= input(question + "(y/n): ").lower().strip()

        if answer in ["y", "yes"]:
            return True 
        elif answer in ["n","no"]:
            return False
        else:
            print("Please enter y or n.")


# Get a number within a spicified range 
def get_number(question,minimum,maximum):
    while True:
        try:
            number = int(input(question))

            if minimum <= number <= maximum:
                return number
            
            print(f"Please enter a number from {minimum} to {maximum}.")

        except ValueErorr:
            print ("Please enter a valid number.")