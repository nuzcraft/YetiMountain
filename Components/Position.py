# class file for position, a component


class Position:
    # defining a position
    # default direction is South (facing down)
    def __init__(self, position_array, direction='South'):
        self.position_array = position_array
        self.direction = direction
