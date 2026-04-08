import random

world_state = {
    "weather": "sunny",
    "event": "normal"
}

def update_world():
    events = ["rain", "festival", "normal"]
    event = random.choice(events)

    world_state["event"] = event

    if event == "rain":
        world_state["weather"] = "rainy"
    else:
        world_state["weather"] = "sunny"

    return world_state
