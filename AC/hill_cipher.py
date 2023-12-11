import numpy as np

def matrix_modulo_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inverse = pow(det, -1, modulus)
    adjugate = det_inverse * np.round(det * np.linalg.inv(matrix)).astype(int)
    inverse_matrix = adjugate % modulus
    return inverse_matrix

def text_to_matrix(text):
    return np.array([ord(char) - ord('A') for char in text])

def matrix_to_text(matrix):
    return ''.join([chr(num + ord('A')) for num in matrix])

def hill_cipher_encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    if len(plain_text) % n != 0:
        raise ValueError("Length of plain text must be a multiple of the key matrix size")

    encrypted_text = ""
    for i in range(0, len(plain_text), n):
        block = text_to_matrix(plain_text[i:i+n])
        encrypted_block = np.dot(block, key_matrix) % 26
        encrypted_text += matrix_to_text(encrypted_block)

    return encrypted_text

def hill_cipher_decrypt(encrypted_text, key_matrix):
    key_matrix_inverse = matrix_modulo_inverse(key_matrix, 26)

    decrypted_text = ""
    for i in range(0, len(encrypted_text), 2):
        block = text_to_matrix(encrypted_text[i:i+2])
        decrypted_block = np.dot(block, key_matrix_inverse) % 26
        decrypted_text += matrix_to_text(decrypted_block)

    return decrypted_text

# Get the key matrix from the user
key_matrix_str = input("Enter the 2x2 key matrix (e.g., '3 7 8 11'): ")
key_matrix = np.array([int(num) for num in key_matrix_str.split()]).reshape(2, 2)

# Get the plaintext from the user
plaintext = input("Enter the plaintext (in uppercase): ")

# Encrypt the plaintext
encrypted_text = hill_cipher_encrypt(plaintext, key_matrix)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix)
print(f"Decrypted Text: {decrypted_text}")