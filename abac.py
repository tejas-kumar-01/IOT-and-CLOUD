def check_access(role, data_type):
    policies = {
        "doctor": ["heart_rate", "temperature", "full"],
        "coach": ["fatigue"],
        "analyst": ["anonymized"]
    }

    return data_type in policies.get(role, [])