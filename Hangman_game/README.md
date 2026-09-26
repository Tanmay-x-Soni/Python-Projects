# Hangman

A simple **Hangman word-guessing game** built with Python.

## About

The player has to guess a hidden word one letter at a time.

For every incorrect guess, part of the hangman is drawn. The player wins by guessing the word before all the lives are used.

## How It Works

- The program randomly selects a word.
- The hidden word is displayed using blank spaces.
- The player guesses one letter at a time.
- Correct guesses reveal the letters.
- Incorrect guesses reduce the remaining lives.
- The game ends when the player guesses the word or runs out of lives.

## Concepts Used

- Python variables
- `input()`
- `if / elif / else`
- `while` loops
- `for` loops
- Lists
- Strings
- Random selection
- Functions
- Basic game logic

## Project Structure

```text
Hangman_game/
├── Hangman.py
├── Hangman_art.py
└── Words.py
```

## How to Run

Make sure Python is installed, then run:

```bash
python Hangman.py
```

## Project Type

**Beginner Python Project**

Part of my Python learning journey with the **100 Days of Code** course.