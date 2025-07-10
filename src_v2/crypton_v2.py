# src crypton_v2.py (Caesar/XOR/Vigenère)

# Caesar Cipher
def caesar_shift(char, key):
    if char.isupper():
        base = ord('A')
    elif char.islower():
        base = ord('a')
    else:
        return char
    return chr((ord(char) - base + key) % 26 + base)

def caesar_encrypt(text, key):
    return ''.join(caesar_shift(c, key) for c in text)

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

# XOR Cipher (same fn for enc/dec)
def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

# Vigenère Cipher
def vigenere_shift(char, key_char, decrypt=False):
    if not char.isalpha():
        return char
    base = ord('A') if char.isupper() else ord('a')
    k = ord(key_char.lower()) - ord('a')
    if decrypt:
        k = -k
    return chr((ord(char) - base + k) % 26 + base)

def vigenere(text, keyword, decrypt=False):
    result, j = [], 0
    for c in text:
        if c.isalpha():
            result.append(vigenere_shift(c, keyword[j % len(keyword)], decrypt))
            j += 1
        else:
            result.append(c)
    return ''.join(result)

# Main Menu
def show_banner():
    print(r'''
  /$$$$$$                                  /$$
 /$$__  $$                                | $$
| $$  \__/  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$
| $$       /$$__  $$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$| $$__  $$
| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$| $$  \ $$
| $$    $$| $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$  | $$
|  $$$$$$/| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$/| $$  | $$
 \______/ |__/       \____  $$| $$____/    \___/   \______/ |__/  |__/
                     /$$  | $$| $$
                    |  $$$$$$/| $$
                     \______/ |__/

            🔐 Welcome to Crypton v2 🔐
==================================================
    Caesar · XOR · Vigenère Encryption Tool
==================================================
''')

def show_menu():
    print("1) Caesar Encrypt")
    print("2) Caesar Decrypt")
    print("3) XOR Encrypt/Decrypt")
    print("4) Vigenère Encrypt")
    print("5) Vigenère Decrypt")
    print("0) Exit")

def main():
    show_banner()
    while True:
        show_menu()
        choice = input("Choice: ").strip()

        if choice == '0':
            print("Exiting Crypton... Stay safe out there.")
            break

        text = input("Enter text: ")

        if choice in {'1', '2'}:
            key = int(input("Enter shift (int): "))
            if choice == '1':
                print("Encrypted:", caesar_encrypt(text, key))
            else:
                print("Decrypted:", caesar_decrypt(text, key))

        elif choice == '3':
            key = int(input("Enter XOR key (int 0-255): "))
            print("Result:", xor_encrypt_decrypt(text, key))

        elif choice in {'4', '5'}:
            keyword = input("Enter keyword (letters only): ").strip()
            if not keyword.isalpha():
                print("Keyword must contain only letters.")
                continue
            decrypt = (choice == '5')
            result = vigenere(text, keyword, decrypt)
            print("Result:", result)

        else:
            print("Invalid choice.")

        confirm = input("\nDo you want to exit? (y/n): ").strip().lower()
        if confirm == 'y':
            print("Exiting Crypton... Keep encrypting.")
            break
        print("\n")

if __name__ == "__main__":
    main()