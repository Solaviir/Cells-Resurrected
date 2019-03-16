import unittest
import config
from cells.models.Plant import Plant
from cells.models.Position import Position
# From root of project, can run unit tests by
# 'python -m unittest cells/tests/models/Plant.py'


class TestPlant(unittest.TestCase):

    # Tests plant initializer for creating new position, having the correct starting energy
    def test__init(self):
        new_plant: Plant = Plant(Position(4, 10))
        self.assertEqual(new_plant.position.x, 4)
        self.assertEqual(new_plant.position.y, 10)
        self.assertEqual(new_plant.energy, config.PLANT_STARTING_ENERGY)

    # Tests that after running increment turn, the plant's energy is the correct new amount
    def test__increment__turn(self):
        new_plant: Plant = Plant(Position(7, 20))
        old_energy: int = new_plant.energy
        new_plant.increment_turn()
        self.assertEqual(new_plant.energy, old_energy
                         + new_plant.energry_recovery_rate)


if __name__ == '__main__':
    unittest.main()
