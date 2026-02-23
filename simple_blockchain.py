# Import required libraries
import hashlib   # For hashing the block contents
import time      # To timestamp the block creation

# ---- DEFINE BLOCK CLASS ----
class Block:

    # Constructor to initialize a block
    def __init__(self, index, data, previous_hash):
        self.index = index                    # Block position in the chain
        self.timestamp = time.time()          # Time when block was created
        self.data = data                      # Data or information stored in the block
        self.previous_hash = previous_hash    # Hash of the previous block in the chain
        self.hash = self.compute_hash()       # Hash of this block

    # Method to compute the hash of the block
    def compute_hash(self):
        # Combine block attributes as a single string
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        # Encode string to bytes and compute SHA-256 hash
        return hashlib.sha256(block_string.encode()).hexdigest()


# ---- CREATE THE FIRST BLOCK ----
# Genesis Block has index 0 and previous hash as "0"
genesis_block = Block(0, "Genesis Block", "0")

# ---- PRINT GENESIS BLOCK HASH ----
print("Genesis Block Hash:", genesis_block.hash)
