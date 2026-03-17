# Classical Ciphers

A Python implementation of three classical substitution ciphers with both encryption and decryption. Built to explore foundational cryptographic concepts including symmetric encryption, key-based encoding, and algorithm design.

## Ciphers

Caesar Cipher
Shifts each letter in the message by a fixed number of positions in the alphabet. The default rotation is 13 (also known as ROT13). Decryption reverses the shift.

Atbash Cipher
Substitutes each letter with its mirror in the alphabet (A↔Z, B↔Y, etc.). The cipher is self-reversing — running it twice returns the original message.

Vigenère Cipher
An extension of the Caesar cipher that uses a keyword instead of a fixed rotation. Each letter in the message is shifted by the corresponding letter in the repeating keyword, making it significantly harder to crack than a simple Caesar cipher.

## Usage
python ciphers.py

You will be prompted to choose a cipher and enter your message:

Enter your message: Hello World

Cipher options:
  1. Atbash
  2. Caesar
  3. Vigenere

Enter choice: 2

How many rotations? (default is 13): 3
Ciphered:   Khoor Zruog
Deciphered: Hello World

## Concepts Covered

- Symmetric encryption
- Key-based encoding
- Substitution cipher design
- Encryption and decryption algorithm implementation

## Requirements

Python 3.x — no external libraries required.
