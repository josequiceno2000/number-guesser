import random
import time
import json
import os

# High Score File
HS_FILE = "high_scores.json"

def load_high_scores():
    if os.path.exists(HS_FILE):
        try:
            with open(HS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            pass

    # Default high scores
    return {
        "EASY": None,
        "MEDIUM": None,
        "HARD": None
    }

def save_high_scores(high_scores):
    with open(HS_FILE, "w") as file:
        json.dump(high_scores, file, indent=4)

def welcome():
    # Number Selection
    chosen_number = random.randint(1, 100)

    # Welcome Message
    print("Welcome to the number guessing game!")
    print("Try to guess the number I'm thinking of [between 1 and 100].")

    # High Score Display
    high_scores = load_high_scores()
    print("\nCurrent High Scores:")
    for diff, score in high_scores.items():
        if score:
            print(f" {diff}: {score['attempts']} attempts in {score['time']:.2f} seconds")
        else:
            print(f" {diff}: No high score yet.")

    # Difficulty Selection
    difficulty_selection = input("\nChoose a difficulty. \n1: EASY\n2: MEDIUM\n3: HARD\n> ").lower()
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

    return (user_attempts, difficulty, chosen_number)

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

def get_hint(chosen_number: int):
    hints = []

    # Even or Odd Hint
    if chosen_number % 2 == 0:
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")

    # Divisibility Hints
    for i in range(3, 11):
        if chosen_number % i == 0:
            hints.append(f"The number is divisible by {i}.")

    return random.choice(hints)

def main():
    try_again = True

    while try_again:
        user_attempts_remaining, difficulty, chosen_number = welcome()

        user_attempts = 1

        start_time = time.time()    

        while user_attempts_remaining > 0:
            if user_attempts == 3:
                user_get_hint_choice = input("\nWould you like a hint? Type 'h' for YES or any other key for NO:\n> ").lower()
                if user_get_hint_choice == 'h':
                    hint = get_hint(chosen_number)
                    print(f"\n[HINT]: {hint}")
                else:
                    print("\nAlrighty. Continue guessing.")

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

        # High Score Update
        if result == 0:
            high_scores = load_high_scores()
            current_record = high_scores.get(difficulty)

            is_new_high = False
            if current_record is None:
                is_new_high = True
            elif user_attempts < current_record['attempts']:
                is_new_high = True
            elif user_attempts == current_record['attempts'] and total_time < current_record['time']:
                is_new_high = True
            
            if is_new_high:
                print(f"🎉 New High Score for {difficulty}!")
                high_scores[difficulty] = {
                    "attempts": user_attempts,
                    "time": total_time
                }
                save_high_scores(high_scores)


        
        
        play_again = input("\nDo you want to play again? Type 'y' for YES or 'n' for NO:\n> ").lower()
        if play_again == 'y':
            continue
        else:
            print("\nThank you for playing! Goodbye.")
            try_again = False
    

if __name__ == "__main__":
    main()