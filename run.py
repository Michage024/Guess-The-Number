# src/main.py

import random


def play_game():
    number_to_guess = random.randint(1, 7)
    attempts = 0
    max_attempts = 5
    guessed = False

    print("\nWelcome to the Guess the Number Game!")
    print(f"I have selected a number between 1 and 7.")
    print(f"Guess the number I have selected and type it in.")
    print(f"You have {max_attempts} attempts to guess the right number.")

    while not guessed and attempts < max_attempts:
        try:
            guess = int(input("Type in your number: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                guessed = True
                print(f"Well done! You guessed the correct number in ")
                print(f"{attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

    if not guessed:
        print(f"Sorry, you have used all {max_attempts} attempts.")
        print(f"The correct number is {number_to_guess}.")


def main():
    while True:
        play_game()
        play_again = input("Would you like to play again?")
        play_again = input("(yes/no):").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing the Guess the Number Game!")
            break


if __name__ == "__main__":
    main()
