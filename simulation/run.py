from simulation.world import update_world
from simulation.hub import send_event_to_npcs
from simulation.npc import NPC

npcs = [NPC("Alex"), NPC("Sam"), NPC("Jordan")]

def run_simulation():
    world = update_world()
    directive = send_event_to_npcs(world)

    reactions = [npc.react(directive) for npc in npcs]

    return {
        "world": world,
        "reactions": reactions
    }
