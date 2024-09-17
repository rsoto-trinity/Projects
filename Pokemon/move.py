# Define the Move classes
class Move:
    def __init__(self, name, move_type, power, accuracy, category, status_effect=None, status_chance=0, recoil=0, flinch_chance=0):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.status_effect = status_effect
        self.status_chance = status_chance
        self.recoil = recoil
        self.flinch_chance = flinch_chance
        self.charge_turns = 0