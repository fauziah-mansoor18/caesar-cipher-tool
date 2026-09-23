# Caesar Cipher Tool 🔐

A simple Python-based Caesar Cipher tool that allows users to encrypt and decrypt messages using a shift value.

## Features

- Encrypt messages using Caesar Cipher
- Decrypt encrypted messages
- Supports uppercase and lowercase letters
- Preserves spaces, numbers, and special characters
- Handles alphabet wrap-around
- Allows the user to choose encryption or decryption

## Technologies Used

- Python
- `input()`
- Conditional Statements
- `for` Loops
- String Methods
- `ord()`
- `chr()`
- Modulo Operator `%`

## How It Works

1. The user enters a message.
2. The user enters a shift value.
3. The user chooses encryption (`E`) or decryption (`D`).
4. The program processes each character.
5. Letters are shifted according to the selected operation.
6. Spaces, numbers, and special characters remain unchanged.
7. The final encrypted or decrypted message is displayed.

## Example

### Encryption

```text
Enter your message: CAT
Enter shift value: 2
Enter E for encryption or D for decryption: E

Encrypted message: ECV

Decryption
Enter your message: ECV
Enter shift value: 2
Enter E for encryption or D for decryption: D

Decrypted message: CAT

Concepts Learned
This project helped me understand:
User input
Variables
if, elif, and else
for loops
String methods
ord() and chr()
Character shifting
Modulo operator
Basic encryption and decryption concepts
Important Note
Caesar Cipher is a simple classical cipher and is not considered secure for modern cybersecurity applications. This project is created for learning basic encryption and decryption concepts.
Author
Fauziah Mansoor