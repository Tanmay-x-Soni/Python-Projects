# Caesar Cipher

A simple **Caesar Cipher** program built with Python.

## About

The Caesar Cipher is a basic encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet.

This program allows the user to **encrypt** a message and **decrypt** it using a chosen shift amount.

## How It Works

- The user chooses whether to **encode** or **decode** a message.
- The program takes the message and a shift number.
- Each letter is shifted through the alphabet.
- The resulting message is displayed.
- The program can handle shifts that go beyond the end of the alphabet.

### Example

With a shift of `3`:

```text
Original:  hello
Encoded:   khoor
```

Decoding `khoor` with the same shift gives:

```text
hello
```

## Concepts Used

- Python variables
- `input()`
- Strings
- Lists
- `for` loops
- `if / else`
- Functions
- String indexing
- Basic encryption logic
- Modular arithmetic

## How to Run

Make sure Python is installed, then run:

```bash
python caesar_cipher.py
```

## Project Type

**Beginner Python Project**

Part of my Python learning journey with the **100 Days of Code** course.