# BlockChain

### Custom Python Blockchain

Welcome to your personal blockchain — a simplified but functional cryptocurrency prototype built from scratch in Python. This project explores the foundations of blockchain architecture including hashing, mining, wallet cryptography, and transaction validation.

##  Overview

This educational blockchain system replicates core mechanisms used in real-world cryptocurrencies like Bitcoin:

-  Wallets using RSA key pairs  
-  Proof-of-work mining  
-  Block integrity via SHA-256 hashing  
-  Signed transactions between wallets  
-  Blockchain validity checks


## Why This Exists

Blockchain often feels like magic. This project was built to demystify it — to show how hashing, validation, mining, and cryptography **actually work** under the hood. All logic is written manually, no blockchain libraries used.


## Project Structure

BlockChain/
├── blockchain.py # Core Block and Blockchain classes
├── miner.py # Handles proof-of-work mining operations
├── node.py # Simulates a decentralized blockchain node
├── transaction.py # Handles transaction structure and digital signatures
├── wallet.py # Generates public/private key pairs
├── test_blockchain.py # Tests basic chain flow: create, transact, mine
├── test_all.py # Runs full-chain simulation including node interaction
├── public_key.pem # RSA public key (safe to share)
├── private_key.pem # RSA private key (keep secret)
├── requirements.txt # Python package dependencies
├── .gitignore # Ignores keys/pycache in repo
└── README.md # This file

## How to Run

1. Clone the repo
git clone https://github.com/dclemens78/YourRepoName.git
cd YourRepoName

2. Install required libraries
pip install requirements.txt

3. Run Node.py
sets up server

4. Generate your wallet (RSA keypair)
python wallet.py

This creates:

public_key.pem — used to receive transactions
private_key.pem — used to sign transactions (keep it secure)

5. Run the blockchain simulation
python test_blockchain.py

This will:

  - Generate a genesis block
  - Add signed transactions
  - Mine blocks with proof-of-work
  - Output the full blockchain to console

## How Transactions Work

  - Transactions are signed using your private key
  - The blockchain verifies the signature using the sender's public key
  - Only valid, signed transactions are added to blocks

## How Mining Works

  - Each block must have a hash that starts with a target number of zeroes (difficulty)
  - Miners increment the nonce until a valid hash is found
  - Once mined, the block is added to the chain and verified

## Blockchain Validation
  - Every time a new block is added, the chain runs:
  - is_valid_chain() to ensure block hashes and previous links are correct
  - Signature validation to ensure transactions are legitimate

## Limitations (by design)
  - No networking — this is a local blockchain, no peer-to-peer
  - No database — everything is in-memory
  - No actual cryptocurrency — just printed confirmation of balance/ownership
  - No mempool — all transactions go directly into a block

## Future Features (stretch goals)
   - Flask API and web wallet interface
   - P2P node communication
   - Transaction pool & smart contract hooks
   - Blockchain explorer (frontend)
     

# Example Output
Mining...
Block added: 00000298f... (nonce: 328491)
Transaction: Alice → Bob | Amount: 10
Signature verified: VALID
Chain length: 3 blocks

## License
MIT License — Free to use, modify, and learn from.

## Acknowledgement
This project was inspired by the original C++ Bitcoin source code, developed by Satoshi Nakamoto in 2009

##IMPORTANT NOTE FROM CREATOR

Hello readers. I appreciate all of you who have cloned this repo. I would just like to iterate however, that I currently have NO PLANS of adding utility to these coins, meaning you will not make money from mining them. This project was created due to my admiration for the original bitcoin source code, and growing admiration for blockchain technology. I plan to keep creating unique Python projects both related to crypto and AI/ML. If you have any suggestions or would like to expand upon this project with me, please reach out. 
Email: danielcle0708@gmail.com

Thank you all for your interest!

- Danny Clemens, Aspiring AI engineer

