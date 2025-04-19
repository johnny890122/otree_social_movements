import json, random

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

def num_revolt_participants(player) -> int:
    is_practice = True if player.round_number == 1 else False

    num_participants = 0
    if is_practice:
        network_data = load_network_data(player.session.config["network"])
        for node in network_data["nodes"]:
            if node["example_join_revolt"]:
                num_participants += 1
    else:
        for p in player.group.get_players():
            if p.revolt:
                num_participants += 1

    return num_participants


def revolt_success(player) -> bool:
    
    is_practice = True if player.round_number == 1 else False

    if is_practice:
        network_data = load_network_data(player.session.config["network"])
        revolt_success = network_data.get("revolt_success", False)
    else:
        num_participants = num_revolt_participants(player)
        rewards_data = load_rewards_data()

        for reward in rewards_data:
            if reward["participants"] == num_participants:
                prob_success = reward["probSuccess"]
                break
        
        revolt_success = random.random() < prob_success

    
    return revolt_success

def join_revolt(player) -> bool:
    is_practice = True if player.round_number == 1 else False

    if is_practice:
        network_data = load_network_data(player.session.config["network"])
        for node in network_data["nodes"]:
            if node["id"] == player.my_label:
                join_revolt = node["example_join_revolt"]
                break
    else:
        join_revolt = player.revolt

    return join_revolt

def get_reard_loss_from_game(num_participants: int) -> tuple:
    if num_participants == 0:
        return 0, 0
    
    rewards_data = load_rewards_data()
    for reward in rewards_data:
        if reward["participants"] == num_participants:
            return reward["rewardSuccess"], reward["lossFailed"]
