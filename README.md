# Guess The Number

### User Experience
"Guess the Number" is a simple text-based game where the player has to guess a randomly generated number between 1 and 7. The game provides feedback whether the guess is too high, too low, invalid due to an out of range number entered, invalid due to a repeated wrong number entered or correct. The player has a maximum of 5 attempts to guess the number correctly. After the game ends, the player is given the option to play again.

### How to Run

User needs to ensure that they have Python 3.x installed on their device.

Save the provided code in a file named run.py.

Open a terminal or command prompt.

Navigate to the directory where run.py is located.

Run the game using the following command:

python run.py

### User Functions Steps:

If User enters a number that is below the correct 'number_to_guess', it prints 'Too low!' and prompts User to enter a different number.

The image below shows an example:

![welcome](https://github.com/user-attachments/assets/f0003940-09ca-4a14-b20a-b444444fd821)

If User enters a number that is higher than the correct 'number_to_guess', it prints 'Too high!' and prompts User to enter a different number.

The image below shows an example:

![too high](https://github.com/user-attachments/assets/2357c186-bc1a-48e8-a6b7-69b7b1706257)

If User is enters the correct number, 'Well done! You guessed the correct number in (the amount of attempts) attempts' and prompts User to enter either yes or no to indicate if they will like to play again.

The image below shows an example:

![correct](https://github.com/user-attachments/assets/ee4124f1-eb0f-4651-a77d-1923a4e51358)

If User is unsuccessful after 5 attempts, it prints 'Sorry, you have used all 5 attempts!', then states the correct number and prompts User to enter either yes or no to indicate if they will like to play again.

The image below shows an example:

![Attempts exhausted](https://github.com/user-attachments/assets/18ff8063-cdd6-47f1-ade5-05974cbed1af)

If User enters a wrong number more than once consecutively, it prints 'Sorry, you have used all 5 attempts!' and prompts User to enter a different number.

The image below shows an example:

![wrong number more than once](https://github.com/user-attachments/assets/178d6b66-0baf-4b2f-9b63-284361394f93)

If User enters a number outside of range of numbers from 1 to 7, it prints 'Invalid, please enter a number between 1 and 7!' and prompts User to enter a different number.

The image below shows an example:

![Outside of range of numbers from 1 to 7](https://github.com/user-attachments/assets/b9d468fa-fad8-4ab6-8ef0-c6716fa0105d)

## Features

Randomly selects a number between 1 and 7.

Prompts the player to guess the number.

Informs the player if their guess is too high, too low, or correct.

Keeps track of the number of attempts.

Limits the player to 5 attempts.

Counts invalid entries (numbers outside the range) as attempts.

Prevents the player from guessing the same number more than once.

Offers the player the option to play again after each game.

## Technology

### Requirements

Github

Gitpod

Python 3.x

Heroku

CI Python Linter

### Verification

Code verified with CI Python Linter

Verificator link: https://pep8ci.herokuapp.com/#
