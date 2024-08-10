def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result

def main():
    while True:
        mode = input("Would you like to encrypt or decrypt? (Type 'exit' to quit): ").lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        result = caesar_cipher(text, shift, mode)
        print(f"The resulting text is: {result}\n")

if __name__ == "__main__":
    main()
