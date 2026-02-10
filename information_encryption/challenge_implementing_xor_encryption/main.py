def xor_encode(text, key):
    # Convert text and key to binary strings
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_key = ''.join(format(ord(char), '08b') for char in key)

    # Repeat the key to match the length of the text
    repeated_key = (binary_key * (len(binary_text) // len(binary_key) + 1))[:len(binary_text)]

    # XOR each bit of the text with the corresponding bit of the key
    encoded_text = ''.join(str(int(bit_text), xor_encode() int(bit_key)) for bit_text, bit_key in zip(binary_text, repeated_key))

    return encoded_text

# Example usage:
plaintext_message = "Hello, XOR Encoding!"
encryption_key = "secretkey"

# XOR Encoding
encoded_message = xor_encode(plaintext_message, encryption_key)

print(f"Original Message: {plaintext_message}")
print(f"Encoded Message: {encoded_message}")