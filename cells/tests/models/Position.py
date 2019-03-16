import sys
sys.path.insert(0, '../../models')
import unittest
from cells.models.Position import Position


class TestPosition(unittest.TestCase):

    # Tests the initializer works to set x and y, and that z defaults to 0
    def test__init(self):
        test_position: Position = Position(5, 8)
        self.assertEqual(test_position.x, 5)
        self.assertEqual(test_position.y, 8)
        self.assertEqual(test_position.z, 0)


if __name__ == '__main__':
    unittest.main()
