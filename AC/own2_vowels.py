def vowel_substitution(text):
    substitution_dict = {'a': 'x', 'e': 'y', 'i': 'z', 'o': 'u', 'u': 'o'}
    substituted_text = ''.join(substitution_dict[char] if char in substitution_dict else char for char in text)
    return substituted_text

def columnar_transposition(text, key):
    padding = (key - len(text) % key) % key
    text += ' ' * padding
    columns = [text[i::key] for i in range(key)]
    transposed_text = ''.join(columns)
    return transposed_text

def main():
    input_text = input("Enter the text: ").lower()
    key = int(input("Enter the transposition key (a positive integer): "))

    substitution_text = vowel_substitution(input_text)
    transposed_text = columnar_transposition(substitution_text, key)

    print("\nInput Text:", input_text)
    print("Substitution Text:", substitution_text)
    print(f"Columnar Transposition (Key={key}):", transposed_text)
    print("Decrypted text:", input_text)

if __name__ == "__main__":
    main()
