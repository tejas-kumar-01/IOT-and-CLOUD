import requests
import random
import time

API_URL = "http://127.0.0.1:5000/upload"

players = ["P101", "P102", "P103"]

while True:
    data = {
        "player_id": random.choice(players),
        "heart_rate": random.randint(60, 180),
        "temperature": round(random.uniform(36.0, 40.0), 2),
        "timestamp": time.time()
    }

    try:
        res = requests.post(API_URL, json=data)
        print("Sent:", data, "| Response:", res.json())
    except:
        print("Server not running")

    time.sleep(3)