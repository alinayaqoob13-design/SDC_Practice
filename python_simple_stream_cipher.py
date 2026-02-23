# random module import karte hain jo random number generate karta hai
import random


# Function: keystream generate karega (stream cipher ki tarah)
def generate_keystream(key, length):
    random.seed(key)  # key ko seed banate hain taki same key hamesha same sequence de
    return [random.randint(0, 255)  # 0 se 255 tak ek random number generate karo (ek byte)
            for _ in range(length)]  # jitne message ke characters hain utne hi numbers banao


# Encryption function: XOR + Caesar Shift dono ka use karke
def encrypt(message, key, shift=3):
    message_bytes = [ord(c) for c in message]  # har character ko ASCII value me convert karna
    keystream = generate_keystream(key, len(message))  # message ke length jitna keystream generate karna

    # Step 1: XOR (message byte ^ keystream byte)
    xor_result = [(m ^ k) for m, k in zip(message_bytes, keystream)]

    # Step 2: Caesar shift (+shift) har XOR result pe apply karna
    ciphertext = [(x + shift) % 256 for x in xor_result]
    # % 256 ka matlab hai result hamesha 0-255 range me rahega

    return ciphertext  # ciphertext ek list of numbers ke form me return hoga


# Decryption function: (Reverse Caesar + XOR)
def decrypt(ciphertext, key, shift=3):
    keystream = generate_keystream(key, len(ciphertext))  # same key se wahi keystream phir se generate hoga

    # Step 1: Caesar shift ko reverse karna (yani -shift)
    shifted_back = [(c - shift) % 256 for c in ciphertext]

    # Step 2: XOR dobara keystream ke sath (kyunki XOR reversible hota hai)
    decrypted_bytes = [(c ^ k) for c, k in zip(shifted_back, keystream)]

    return ''.join(chr(b) for b in decrypted_bytes)
    # ASCII numbers ko characters me convert karna aur join karke ek string banana


# Example usage (program run karne ke liye input set karte hain)
message = "HELLO STREAM CIPHER"  # original message
key = 2025  # encryption/decryption key (random generator ke liye)

# Encrypt function call karke message ko ciphertext banate hain
cipher = encrypt(message, key)
print("Ciphertext:", cipher)  # ciphertext ko print karte hain (numbers ki list)

# Decrypt function call karke ciphertext ko wapas original message me convert karte hain
plain = decrypt(cipher, key)
print("Decrypted:", plain)  # decrypted (original) message print karte hain
