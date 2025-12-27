
user_attempts = 3

def welcome():
    print("Welcome to the number guessing game!")
    print("Try to guess the number I'm thinking of [between 1 and 100].")
    print(f"You have {user_attempts} attempts to guess the correct number.")

def main():
    welcome()

if __name__ == "__main__":
    main()