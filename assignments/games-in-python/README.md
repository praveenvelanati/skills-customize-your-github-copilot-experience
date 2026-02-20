# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Create the Game Core

#### Description
Set up the basic game structure with a word list and game state tracking. Initialize variables to store the secret word, guessed letters, and remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Initialize game state with the secret word and attempt counter (e.g., 6 attempts)
- Set up a way to track guessed letters
- Display the hidden word in underscore format (_ _ _ _)

### 🛠️ Handle Player Guesses

#### Description
Implement the logic to accept player guesses, validate them, and update the game state based on correct or incorrect guesses.

#### Requirements
Completed program should:

- Accept single letter guesses from the player
- Check if the letter is in the secret word
- Update the display to show correctly guessed letters
- Decrease attempt counter for wrong guesses
- Prevent duplicate guesses (optional: notify player)

### 🛠️ Implement Game Loop and Win/Lose Conditions

#### Description
Create the main game loop that continues until the player wins or loses, and display appropriate end-game messages.

#### Requirements
Completed program should:

- Run a continuous game loop prompting for guesses
- End the game when the word is completely guessed
- End the game when attempts reach zero
- Display a clear win message when the player guesses the word
- Display a clear lose message showing the secret word when attempts are exhausted
