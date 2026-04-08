class NPC:
    def __init__(self, name):
        self.name = name

    def react(self, directive):
        return f"{self.name} reacts: {directive['action']}"
