import random
import math

def generate_public_key(private_key, multiplier, modulus):
    values = private_key.split(',')
    public_key = ""
    for v in values:
        i = (int(v) * int(multiplier)) % int(modulus)
        if public_key == "":
            public_key += str(i)
        else:
            public_key += "," + str(i)
    return public_key

def find_inverse_multiplier(n, modulus):
    for i in range(5000):
        if ((n * i) % modulus) == 1:
            return i
    return 0

def encrypt_message(public_key, binary_message):
    result = ""
    weights = [int(w) for w in public_key.split(',')]
    ptr = 0

    binary_message = binary_message * (len(weights) // len(binary_message)) + binary_message[:len(weights) % len(binary_message)]

    while ptr < len(binary_message):
        total = 0
        for i in range(len(weights)):
            if ptr < len(binary_message) and binary_message[ptr] == '1':
                bit = 1
            else:
                bit = 0
            total += weights[i] * bit
            ptr += 1

        if result == "":
            result += str(total)
        else:
            result += "," + str(total)

    return result

data_input = input("Enter binary message:")
private_key_input = input("Enter private key (in super increasing order) :")
private_key_values = [int(v) for v in private_key_input.split(',')]
modulus = random.randint(sum(private_key_values) + 1, 100)
print(modulus)
multiplier = 2
while math.gcd(multiplier, modulus) != 1:
    multiplier += 1
print(multiplier)

public_key = generate_public_key(private_key_input, "7", "20")
cipher_text = encrypt_message(public_key, data_input)
inverse_multiplier = find_inverse_multiplier(7, 20)
decrypted_text = generate_public_key(cipher_text, str(inverse_multiplier), str(20))

print("Private key:", private_key_input)
print("Public key:", public_key)
print("Cipher text:", cipher_text)
print("Inverse multiplier:", inverse_multiplier)
print("Decrypted text:", decrypted_text)
print("Decrpted binary message:", data_input)