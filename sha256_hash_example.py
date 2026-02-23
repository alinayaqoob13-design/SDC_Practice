# Import hashlib library for hashing
import hashlib

# ---- DATA TO HASH ----
str = "COMSATS"               # Original string to hash
# .encode() converts string to bytes, required by hashlib
data_bytes = str.encode()

# ---- CREATE SHA-256 HASH OBJECT ----
result = hashlib.sha256(data_bytes)  # Create SHA-256 hash object for the data

# ---- GET HASH IN HEXADECIMAL FORM ----
# .hexdigest() returns the hash as a readable hexadecimal string
print("The sha256 equivalent of hash is :", result.hexdigest())
