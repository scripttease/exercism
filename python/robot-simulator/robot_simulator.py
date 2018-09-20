# Globals for the bearings
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4
        print(self.bearing)

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4
        print(self.bearing)

    def advance(self):
        x_coord = self.coordinates[0]
        y_coord = self.coordinates[1]

        if self.bearing == NORTH:
            self.coordinates = (x_coord, y_coord + 1)
        elif self.bearing == EAST:
            self.coordinates = (x_coord +1, y_coord)
        elif self.bearing == SOUTH:
            self.coordinates = (x_coord, y_coord + -1)
        elif self.bearing == WEST:
            self.coordinates = (x_coord -1, y_coord)
        else:
            self.coordinates = self.coordinates + (0, 0)

    def simulate(self, instructions):
        for i in instructions:
            if i == "R":
                self.turn_right()
            elif i == "L":
                self.turn_left()
            elif i == "A":
                self.advance()
            else:
                return self
