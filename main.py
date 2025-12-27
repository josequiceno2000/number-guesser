import random
import time
import sys

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
    # Take Guess Input
    user_guess = int(input("\nMake your guess:\n> "))
    print(f"You guessed: {user_guess}" )

    # Check Guess
    if user_guess == chosen_number:
        return (0, "Congratulations! You've guessed the correct number!")
    elif user_guess < chosen_number:
        return (1, "Too low.")
    elif user_guess > chosen_number:
        return (1, "Too high.")


def main():
    try_again = True

    while try_again:
        user_attempts_remaining, chosen_number = welcome()

        user_attempts = 1

        start_time = time.time()    

        while user_attempts_remaining > 0:
            result, message = guess(user_attempts_remaining, chosen_number)
            if result == 0:
                print(message)
                break   
            else:
                user_attempts_remaining -= 1
                user_attempts += result
                print(f"\n{message}")
                if user_attempts_remaining > 0:
                    print(f"\nYou have {user_attempts_remaining} attempts remaining. Try again.")
                else:
                    print(f"\nYou've run out of attempts. The correct number was {chosen_number}. Game over.")
        
        end_time = time.time()
        total_time = end_time - start_time
        print(f"\nYou made {user_attempts} attempts.")
        print(f"Total time taken: {total_time:.2f} seconds.")
        
        play_again = input("\nDo you want to play again? Type 'y' for YES or 'n' for NO:\n> ").lower()
        if play_again == 'y':
            continue
        else:
            print("\nThank you for playing! Goodbye.")
            try_again = False
    

if __name__ == "__main__":
    main()