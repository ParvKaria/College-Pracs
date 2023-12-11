def custom_encrypt(plain_text, key):
    # Step 1: Convert plain text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in plain_text)

    # Step 2: Find the 1's complement
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_text)

    # Step 3: Convert binary to hexadecimal
    hex_value = hex(int(ones_complement, 2))[2:]

    # Step 4: Convert to alphabet equivalent
    encrypted_text = ''.join(chr(int(hex_char, 16) + 64) for hex_char in hex_value)

    # Determine the number of rows in the table
    num_rows = (len(encrypted_text) + key - 1) // key

    # Create the table as a list of lists
    table = [['' for _ in range(key)] for _ in range(num_rows)]

    # Fill the table with the encrypted text
    for i, char in enumerate(encrypted_text):
        row = i // key
        col = i % key
        table[row][col] = char

    # Modify specific cells based on the key
    for i in range(key - 1, len(encrypted_text), key):
        row = i // key
        col = i % key
        table[row][col] = chr(ord(table[row][col]) + 1)

    # Convert the table to a string, writing row-wise
    encrypted_table = ''.join(''.join(row) for row in table)

    return encrypted_table

def custom_decrypt(encrypted_text, key):
    # Determine the number of rows in the table
    num_rows = (len(encrypted_text) + key - 1) // key

    # Create the table as a list of lists
    table = [['' for _ in range(key)] for _ in range(num_rows)]

    # Fill the table with the encrypted text
    for i, char in enumerate(encrypted_text):
        row = i // key
        col = i % key
        table[row][col] = char

    # Reverse the modification made during encryption
    for i in range(key - 1, len(encrypted_text), key):
        row = i // key
        col = i % key
        table[row][col] = chr(ord(table[row][col]) - 1)

    # Convert the table to a string, writing row-wise
    decrypted_table = ''.join(''.join(row) for row in table)

    # Convert from alphabet equivalent to hexadecimal
    hex_value = ''.join(hex(ord(char) - 64)[2:] for char in decrypted_table)

    # Convert from hexadecimal to binary
    binary_text = bin(int(hex_value, 16))[2:]

    # Find the 1's complement
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_text)

    # Convert from binary to plain text
    decrypted_text = ''.join(chr(int(ones_complement[i:i + 8], 2)) for i in range(0, len(ones_complement), 8))

    return decrypted_text


while True:
    print("Menu:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        key = int(input("Enter the key (number of columns): "))
        encrypted_text = custom_encrypt(plain_text, key)
        print("Encrypted text:")
        print(encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the encrypted text: ")
        key = int(input("Enter the key (number of columns): "))
        # Implement decryption function (reverse of encryption)
        decrypted_text = custom_decrypt(encrypted_text, key)
        print("Decrypted text:")
        print(decrypted_text)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")