class Position:

    def __init__(self, x, y, z=0):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def move(self, new_x: int, new_y: int, new_z: int):
        self.x = new_x
        self.y = new_y
        self.z = new_z
