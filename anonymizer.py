import hashlib

def anonymize(data):
    player = data.get("player_id", "unknown")   

    anon_id = hashlib.sha256(player.encode()).hexdigest()

    return {
        "anon_id": anon_id,
        "heart_rate": data.get("heart_rate", 0),
        "temperature": data.get("temperature", 0),
        "timestamp": data.get("timestamp", "N/A")
    }