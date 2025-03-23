import json

def load_network_data(config: str) -> dict:
    assert config in ["type_I", "type_II"], "Invalid network configuration"
    file = f"_static/networks/{config}.json"
    with open(file, "r") as f:
        data = json.load(f)

    return data

def load_rewards_data() -> dict:
    file = "_static/rewards.json"
    with open(file, "r") as f:
        data = json.load(f)

    return data