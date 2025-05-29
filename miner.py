# Danny Clemens
#
# miner.py

''' A file that automates the mining of a block every 15 seconds '''

import requests
import time

while True:
    print("Mining block")
    res = requests.get("http://127.0.0.1:5000/mine")
    print("✅", res.json())
    time.sleep(15)  # mine every 15 seconds
