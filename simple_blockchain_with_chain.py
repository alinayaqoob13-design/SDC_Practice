# Import necessary libraries
import hashlib   # For SHA-256 hashing
import time      # To timestamp blocks

# ---- DEFINE BLOCK CLASS ----
class Block:

    def __init__(self, index, data, previous_hash):
        self.index = index                    # Block position in the chain
        self.timestamp = time.time()          # Time when the block was created
        self.data = data                      # Information/data stored in the block
        self.previous_hash = previous_hash    # Hash of the previous block
        self.hash = self.compute_hash()       # Compute hash for this block

    # Method to compute SHA-256 hash of the block
    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"  # Combine block data
        return hashlib.sha256(block_string.encode()).hexdigest()  # Return hash in hexadecimal

# ---- CREATE GENESIS BLOCK (FIRST BLOCK) ----
genesis_block = Block(0, "Genesis Block", "0")  # Index 0 and previous hash "0"
print("Genesis Block Hash:", genesis_block.hash)


# ---- DEFINE BLOCKCHAIN CLASS ----
class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize blockchain with genesis block

    # Create the first block in the chain
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    # Add a new block to the chain
    def add_block(self, data):
        previous_block = self.chain[-1]                   # Get last block in the chain
        new_block = Block(len(self.chain), data, previous_block.hash)  # Create new block
        self.chain.append(new_block)                     # Append new block to the chain

    # Print details of all blocks in the blockchain
    def print_blockchain(self):
        for block in self.chain:
            print("Index:", block.index,
                  "Data:", block.data,
                  "Hash:", block.hash,
                  "Previous Hash:", block.previous_hash)


# ---- CREATE AND TEST BLOCKCHAIN ----
blockchain = Blockchain()                     # Create a blockchain object
blockchain.add_block("First Block Data")      # Add first block
blockchain.add_block("Second Block Data")     # Add second block
blockchain.print_blockchain()                 # Print all blocks in the chain
