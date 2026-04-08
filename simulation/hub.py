def send_event_to_npcs(world_state):
    if world_state["event"] == "rain":
        return {"action": "seek shelter"}
    elif world_state["event"] == "festival":
        return {"action": "celebrate"}
    return {"action": "normal"}
