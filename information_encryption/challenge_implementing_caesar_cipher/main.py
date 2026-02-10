def caesar_cipher(text, key):
    result = ""

    # Loop through each character in the input text
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            start = ord('A') if char.isupper() else ord('a')  # Set the starting point based on uppercase or lowercase
            result += chr((ord(char) - start + key) % 26 + start)  # Apply the Caesar cipher formula
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

# Example Usage:
plaintext = "1WORLD2"  # Change the word for encryption
key = 3
encrypted_text = caesar_cipher(plaintext, key)

# Print the results
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted Text: {encrypted_text}")