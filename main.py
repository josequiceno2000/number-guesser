import random

user_attempts = None

def welcome():
    # Number Selection
    chosen_number = random.randint(1, 100)

    # Welcome Message
    print("Welcome to the number guessing game!")
    print("Try to guess the number I'm thinking of [between 1 and 100].")

    # Difficulty Selection
    difficulty_selection = input("\nChoose a difficulty. \nType '1' for EASY\nType '2' for MEDIUM\nType '3' for HARD:\n> ").lower()
    if difficulty_selection == '1':
        difficulty = 'EASY'
    elif difficulty_selection == '2':
        difficulty = 'MEDIUM'
    elif difficulty_selection == '3':
        difficulty = 'HARD'

    user_attempts = 10 - int(difficulty_selection) * 2
    
    print("\nYou've chosen difficulty level:", difficulty)
    print(f"You have {user_attempts} attempts to guess the correct number.")

    # print(f"\nPssst, the correct number is {chosen_number} (just for testing purposes).")

    return (user_attempts, chosen_number)

def guess(user_attempts: int, chosen_number: int):
    user_guess = input("\nMake your guess:\n> ")
    print(f"You guessed: {user_guess}" )

def main():
    user_attempts, chosen_number = welcome()
    guess(user_attempts, chosen_number)
    

if __name__ == "__main__":
    main()