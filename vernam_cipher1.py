def vernam_cipher(text, key):
    # Ensure the key is at least as long as the text
    if len(key) < len(text):
        raise ValueError("Key must be at least as long as the text.")

    cipher_text = ""
    for t_char, k_char in zip(text, key):
        # XOR the characters
        cipher_char = chr(ord(t_char) ^ ord(k_char))
        cipher_text += cipher_char
    return cipher_text


# Example usage:
plaintext = "HELLO"
key = "XMCKL"  # Key should be random and at least as long as plaintext

# Encrypt
ciphertext = vernam_cipher(plaintext, key)
print("Encrypted:", ciphertext)

# Decrypt (same function)
decrypted_text = vernam_cipher(ciphertext, key)
print("Decrypted:", decrypted_text)