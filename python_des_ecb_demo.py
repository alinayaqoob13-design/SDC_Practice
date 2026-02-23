# Importing necessary libraries from PyCryptodome
from Crypto.Cipher import DES                  # DES encryption algorithm ke liye
from Crypto.Random import get_random_bytes     # Random key generate karne ke liye
from Crypto.Util.Padding import pad, unpad     # Data ko block size ke according pad/unpad karne ke liye

# 8-byte (64-bit) key generate karna — DES algorithm me key size fix hoti hai 8 bytes
key = get_random_bytes(8)

# ---- ENCRYPTION FUNCTION ----
def des_encrypt(data, key):
    # Step 1: DES cipher object create karna ECB (Electronic Codebook) mode me
    cipher = DES.new(key, DES.MODE_ECB)

    # Step 2: Data ko pad karna taki uski length DES block size (8 bytes) ke multiple me ho
    padded_data = pad(data, DES.block_size)

    # Step 3: Padded data ko encrypt karna
    encrypted_data = cipher.encrypt(padded_data)

    # Step 4: Encrypted data return karna
    return encrypted_data

# ---- DECRYPTION FUNCTION ----
def des_decrypt(encrypted_data, key):
    # Step 1: Same key ke sath DES cipher object banana ECB mode me
    cipher = DES.new(key, DES.MODE_ECB)

    # Step 2: Encrypted data ko decrypt karna
    decrypted_padded = cipher.decrypt(encrypted_data)

    # Step 3: Decrypted data me se padding remove karna
    decrypted_data = unpad(decrypted_padded, DES.block_size)

    # Step 4: Clean (original) data return karna
    return decrypted_data

# ---- MAIN PROGRAM ----
data = b'Secret123'                     # Encrypt karne ke liye original data (byte form me)
print("Original Data:", data)           # Original data print karna

encrypted_data = des_encrypt(data, key) # Data ko encrypt karna
print("Encrypted Data:", encrypted_data) # Encrypted (ciphertext) print karna

decrypted_data = des_decrypt(encrypted_data, key)  # Encrypted data ko decrypt karna
print("Decrypted Data:", decrypted_data)           # Decrypted (original) data print karna
