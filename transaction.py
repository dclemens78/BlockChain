# Danny Clemens
#
# transaction.py

''' A file that handles, manages, and regulates all transactions between wallets '''

import json
import base64
from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError

# Sign a transaction dict using a private key
def sign_transaction(transaction_data: dict, private_key: SigningKey) -> str:
    message = json.dumps(transaction_data, sort_keys=True).encode()
    signature = private_key.sign(message)
    return base64.b64encode(signature).decode()

# Verify a transaction's signature using the sender's public key
def verify_transaction(transaction_data: dict, signature: str, public_key: VerifyingKey) -> bool:
    message = json.dumps(transaction_data, sort_keys=True).encode()
    try:
        public_key.verify(base64.b64decode(signature), message)
        return True
    except BadSignatureError:
        return False

def create_signed_transaction(sender_private_key, sender_public_key, recipient_address, amount):
    transaction = {
        "sender": base64.b64encode(sender_public_key.to_string()).decode(),
        "recipient": recipient_address,
        "amount": amount
    }
    signature = sign_transaction(transaction, sender_private_key)
    transaction["signature"] = signature
    return transaction

if __name__ == "__main__":
    from wallet import load_keys, get_address

    priv_key, pub_key = load_keys()
    if not priv_key:
        print("No wallet found. Please run wallet.py first.")
    else:
        recipient = input("Recipient address: ")
        amount = int(input("Amount to send: "))
        tx = create_signed_transaction(priv_key, pub_key, recipient, amount)
        print("\nSigned Transaction:")
        print(json.dumps(tx, indent=2))
        print("\nSignature valid?",
              verify_transaction({k: v for k, v in tx.items() if k != "signature"}, tx["signature"], pub_key))
