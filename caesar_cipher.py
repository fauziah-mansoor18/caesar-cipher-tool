text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Enter E for encryption or D for decryption: ").upper()

result = ""

for char in text:

    if char.isalpha():

        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')

        if choice == "E":
            new_char = chr((ord(char) - start + shift) % 26 + start)

        elif choice == "D":
            new_char = chr((ord(char) - start - shift) % 26 + start)

        else:
            print("Invalid choice.")
            break

        result += new_char

    else:
        result += char


if choice == "E":
    print("Encrypted message:", result)

elif choice == "D":
    print("Decrypted message:", result)