# Danny Clemens
#
# node.py

''' A file that connects the blockchain to a live server '''

# node.py
from flask import Flask, request, jsonify
from blockchain import Blockchain
from transaction import verify_transaction

app = Flask(__name__)
blockchain = Blockchain()

@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    tx = request.get_json()
    if not verify_transaction({k: v for k, v in tx.items() if k != "signature"}, tx["signature"], tx["sender"]):
        return "Invalid Signature", 400
    blockchain.add_transaction(tx)
    return "Transaction will be added to next block", 201

@app.route("/mine", methods=["GET"])
def mine_block():
    result = blockchain.mine_pending_transactions()
    return jsonify(result), 200

@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify([block.to_dict() for block in blockchain.chain]), 200
