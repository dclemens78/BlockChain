# Danny Clemens
#
# wallet.py

''' A file that creates and manages wallets used to store crypto '''

from ecdsa import SigningKey, SECP256k1
import base64

# Generate a new private-public key pair
def generate_keypair():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

# Save the keys to local files
def save_keys(private_key, public_key):
    with open("private_key.pem", "wb") as f:
        f.write(private_key.to_pem())
    with open("public_key.pem", "wb") as f:
        f.write(public_key.to_pem())

# Load keys from saved files
def load_keys():
    try:
        with open("private_key.pem", "rb") as f:
            private_key = SigningKey.from_pem(f.read())
        with open("public_key.pem", "rb") as f:
            public_key = private_key.get_verifying_key()
        return private_key, public_key
    except FileNotFoundError:
        return None, None

# Convert a public key to a wallet address (just simplified Base64 for now)
def get_address(public_key):
    return base64.b64encode(public_key.to_string()).decode()

# Create and display a new wallet if not exists
if __name__ == "__main__":
    priv, pub = load_keys()
    if not priv:
        priv, pub = generate_keypair()
        save_keys(priv, pub)
        print("New wallet created!")
    else:
        print("Existing wallet loaded.")

    print("Public Address (Your Wallet ID):")
    print(get_address(pub))
