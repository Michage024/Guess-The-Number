# src/main.py

import random

def guess_the_number():
    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed = False

        print("\nWelcome to 'Guess the Number' game!")
        print("I have selected a number between 1 and 100.")
        
        while not guessed:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
                else:
                    guessed = True
                    print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            except ValueError:
                print("Please enter a valid integer.")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    guess_the_number()
