import config
from cells.models.Position import Position
from random import randint


class Plant:

    # Declaring class variables, common to all plants
    MAX_ENERGY: int = config.PLANT_MAX_ENERGY

    def __init__(self, position: Position):
        # Declaring member variables that belong to the individual plants
        self.energy: int = config.PLANT_STARTING_ENERGY
        self.position: Position = position
        self.energry_recovery_rate: int = config.BASE_RECOVERY_RATE + \
            randint(config.RECOVERY_DEVIATION * -1,
                    config.RECOVERY_DEVIATION)

    def increment_turn(self):
        self.energy = min(self.energry_recovery_rate +
                          self.energy, self.MAX_ENERGY)
