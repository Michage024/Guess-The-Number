# Guess the Number Game


### 1. Purpose of the Project

The "Guess the Number" game is a simple console-based game where players have to guess a randomly selected number between 1 and 7. The game is designed to provide an engaging and challenging experience by limiting the number of attempts and providing feedback on whether the guess is too high, too low, or correct.

### 2. User Stories

As a visitor, I would like to play the game of number guessing.

As a game player, I would like to know whether the guess is correct or not.

### 3. Features

Randomly selects a number between 1 and 7.

Prompts the player to guess the number.

Provides feedback if the guess is too high, too low, or correct.

Limits the player to 5 attempts.

Invalid entries (numbers outside the range) do not count as part of the 5 attempts.

Prevents the player from guessing the same number more than once.

Offers the player the option to play again after each game.

##### Flow Chart

![Guess the game flow chart](https://github.com/user-attachments/assets/074f261d-c838-4089-a6f1-d4f13cd573ba)

#### Start

Begin the program.

#### Main Loop

Prompt: "Would you like to play again? (yes/no): "

Input: play_again

Decision: play_again == 'yes'?

  - If Yes, proceed to Play Game.

  - If No, go to End.

#### Play Game

Set number_to_guess to a random number between 1 and 7.

Initialize attempts to 0.

Initialize max_attempts to 5.

Set guessed to False.

Initialize previous_guesses as an empty set.

Print welcome message and instructions.

#### Guess Loop

While not guessed and attempts < max_attempts:

  - Prompt: "Type in your number: "

  - Input: guess

  - Increment attempts by 1.

  - Decision: guess is a valid integer?

    - If No, print "Please enter a valid integer." and continue.

    - If Yes:

      - Decision: guess < 1 or guess > 7?

        - If Yes, print "Invalid, please enter a valid number" and continue.

        - If No:

          - Decision: guess in previous_guesses?

            - If Yes, print "Invalid, please enter a different number" and continue.

            - If No:

              - Add guess to previous_guesses.

              - Decision: guess < number_to_guess?

                - If Yes, print "Too low!" and continue.

                - If No:

                  - Decision: guess > number_to_guess?

                    - If Yes, print "Too high!" and continue.

                    - If No:

                      - Set guessed to True.

                      - Print "Well done! You guessed the correct number in {attempts} attempts."

#### Max Attempts Reached

Decision: guessed == False?

If Yes, print "Sorry, you have used all {max_attempts} attempts. The correct number is {number_to_guess}."

If No, proceed to Main Loop.

#### End

Print "Thanks for playing the Guess the Number Game!"

End the program.

### 4. Future Features

Implement difficulty levels with different ranges of numbers.

Add a scoring system based on the number of attempts.

Provide hints to the player if they are close to the correct number.

Create a graphical user interface (GUI) for the game.

Allow multiplayer mode where players take turns guessing.

### 5. Technology

Python 3.x

Heroku

Github

Gitpod

CI Python Linter

![heroku](https://github.com/user-attachments/assets/ab6b1a32-da5a-4877-8e30-f26a02f92496)
![gitpod](https://github.com/user-attachments/assets/7804e5d7-86f8-4285-a3b4-a4054711bbe9)

### 6. Testing

#### 6.1 Code Validation

Code runs without errors using Python 3.x.

Code verified with CI Python Linter

Verificator link: https://pep8ci.herokuapp.com/#

![VALIDATION](https://github.com/user-attachments/assets/3bd9f09a-2aff-493e-ac06-4a6b912edf56)

Ligthouse

![light house](https://github.com/user-attachments/assets/d5ec2ecd-be38-49ac-9430-52c77c40496a)

#### 6.2 Test Cases (User Story Based with Screenshots)

#### Test Case 1: Valid Guess

Opening message:

![welcome](https://github.com/user-attachments/assets/f0003940-09ca-4a14-b20a-b444444fd821)

If User enters a number that is below the correct 'number_to_guess', it prints 'Too low!' and prompts User to enter a different number.

The image below shows an example:

![1](https://github.com/user-attachments/assets/c55d21ce-3987-474d-90f6-66b5285e77a3)

If User enters a number that is higher than the correct 'number_to_guess', it prints 'Too high!' and prompts User to enter a different number.

The image below shows an example:

![too high](https://github.com/user-attachments/assets/2357c186-bc1a-48e8-a6b7-69b7b1706257)

If User enters the correct number, it prints 'Well done! You guessed the correct number in (the amount of attempts) attempts' and prompts User to enter either yes or no to indicate if they will like to play again.

The image below shows an example:

![correct](https://github.com/user-attachments/assets/ee4124f1-eb0f-4651-a77d-1923a4e51358)

#### Test Case 2: Invalid Guess

If User enters a number outside the range of numbers from 1 to 7, it prints 'Invalid, please enter a number between 1 and 7!' and prompts User to enter a different number.

The image below shows an example:

![Outside of range of numbers from 1 to 7](https://github.com/user-attachments/assets/cc19916f-def2-44dd-82c8-972f2ea81438)

If User enters any letter or symbol, it prints 'Invalid, please enter a valid integer', and prompts User to enter a different number. These attempts do not affect the 5 limited attempts and can be entered as much as possible.

![symbols](https://github.com/user-attachments/assets/bef61b7e-4233-4f0f-9d2b-5a00fe87116d)

#### Test Case 3: Repeated Guess

If User enters a wrong number more than once consecutively, it prints 'Invalid, please enter a different number between 1 and 7' and prompts User to enter a different number.

The image below shows an example:

![wrong number more than once](https://github.com/user-attachments/assets/178d6b66-0baf-4b2f-9b63-284361394f93)

#### 6.3 Fixed Bugs

Fixed a bug where the game did not count invalid inputs as attempts.

Fixed a bug where repeated guesses were not properly handled.

### 7. Deployment

#### 7.1 Via Gitpod

Open Gitpod and clone the repository.

Ensure Python 3.x is installed in the Gitpod environment.

Navigate to the directory containing main.py.

Run the game using the command:

bash

Copy code

python main.py

#### 7.2 Via Heroku

Create a new Heroku application.

Add the necessary buildpacks for Python.

Deploy the code to Heroku.

Set up a web dyno to run the main.py file.

### 8. Credits

Developed by Michael Agesse.

Inspired by classic number guessing games.

Random number generation powered by Python's random module.

https://www.w3schools.com

This README.md provides detailed information about the "Guess the Number" game, including purpose, user stories, features, future 
enhancements, technologies used, testing methods, deployment instructions, and credits.
