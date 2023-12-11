def encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                char_code = ord(char) - ord('A')
                encrypted_char = (a * char_code + b) % 26 + ord('A')
                ciphertext += chr(encrypted_char)
            elif char.islower():
                char_code = ord(char) - ord('a')
                encrypted_char = (a * char_code + b) % 26 + ord('a')
                ciphertext += chr(encrypted_char)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, a, b):
    a_inverse = 0
    for i in range(26):
        if (i * a) % 26 == 1:
            a_inverse = i
            break
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                char_code = ord(char) - ord('A')
                decrypted_char = (a_inverse * (char_code - b)) % 26 + ord('A')
                plaintext += chr(decrypted_char)
            elif char.islower():
                char_code = ord(char) - ord('a')
                decrypted_char = (a_inverse * (char_code - b)) % 26 + ord('a')
                plaintext += chr(decrypted_char)
        else:
            plaintext += char
    return plaintext

while True:
    print("Affine Cipher Menu:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        plaintext = input("Enter the plaintext: ")
        a = int(input("Enter the value of 'a' (must be coprime with 26): "))
        b = int(input("Enter the value of 'b': "))
        encrypted_text = encrypt(plaintext, a, b)
        print("Encrypted text:", encrypted_text)
    elif choice == "2":
        ciphertext = input("Enter the ciphertext: ")
        a = int(input("Enter the value of 'a' (must be coprime with 26): "))
        b = int(input("Enter the value of 'b': "))
        decrypted_text = decrypt(ciphertext, a, b)
        print("Decrypted text:", decrypted_text)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
