from blockchain import Blockchain

# Step 1: Create blockchain instance
chain = Blockchain()

# Step 2: Add some fake transactions
chain.add_new_transaction({"sender": "Danny", "recipient": "Bob", "amount": 10})
chain.add_new_transaction({"sender": "Alice", "recipient": "Danny", "amount": 5})

# Step 3: Mine a block
print("⛏️ Mining block...")
block_index = chain.mine()
print(f"Block {block_index} mined!\n")

# Step 4: Show the full chain
print("🔗 Full Blockchain:\n")
for block in chain.chain:
    print(f"Block {block.index} - Hash: {block.hash}")
    print(f"  Previous Hash: {block.previous_hash}")
    print(f"  Transactions: {block.transactions}")
    print(f"  Nonce: {block.nonce}")
    print("-----------")