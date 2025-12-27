import random

user_attempts = 3

def welcome():
    chosen_number = random.randint(1, 100)
    print("Welcome to the number guessing game!")
    print("Try to guess the number I'm thinking of [between 1 and 100].")
    print(f"You have {user_attempts} attempts to guess the correct number.")

    print(f"\nPssst, the correct number is {chosen_number} (just for testing purposes).")

def main():
    welcome()

if __name__ == "__main__":
    main()