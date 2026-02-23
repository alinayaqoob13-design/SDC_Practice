# Import hashlib library for hashing
import hashlib

# ---- DATA TO HASH ----
# b'COMSATS' -> converting string to bytes (hash functions need byte input)
data = b'COMSATS'

# ---- CREATE MD5 HASH OBJECT ----
result = hashlib.md5(data)  # Create MD5 hash object for the data

# ---- GET HASH IN BYTE FORM ----
# .digest() returns the hash as bytes
print("The byte equivalent of hash is :", result.digest())
