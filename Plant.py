import config
from Position import Position
import random


class Plant:

    # Declaring class variables, common to all plants
    MAX_ENERGY: int = config.PLANT_MAX_ENERGY

    def __init__(self, position: Position):
        # Declaring member variables that belong to the individual plants
        self.energy: int = config.PLANT_STARTING_ENERGY
        self.position: Position = position
        self.energry_recovery_rate: int = 15 + random.randint(-10, 10)

    def increment_turn(self):
        self.energy = min(self.energry_recovery_rate +
                          self.energy, self.MAX_ENERGY)
