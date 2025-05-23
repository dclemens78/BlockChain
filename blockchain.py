# Danny Clemens
#
# blockchain.py

''' A file that contains the blockchain and regulates how it operates '''

import hashlib
import json
from datetime import datetime, timezone


# individual blocks
class Block:
    
    # index: blocks position in the chain
    # transactions: records transactions for that block
    # timestamp: when the block was created
    # previous_hash: the block before the current block
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash() 

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest() 
    
    
# The entire blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    # genesis block is the first block in the chain!
    def create_genesis_block(self):
        genesis_block = Block(0, [], str(datetime.now(timezone.utc)), "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]
    
   
    def add_block(self, block, proof):
        previous_hash = self.get_last_block().hash
        if previous_hash != block.previous_hash:
            return False 
        if not self.is_valid_proof(block, proof): 
            return False
        block.hash = proof 
        self.chain.append(block)
        return True


    def proof_of_work(self, block, difficulty=2):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash


    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)
    
    def is_valid_proof(self, block, block_hash):
        return block_hash.startswith('00') and block_hash == block.compute_hash()
    
    # We create a new block after each mine
    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.get_last_block()
        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=str(datetime.now(timezone.utc)), 
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index
