# class file for position, a component


class Position:
    # defining a position
    def __init__(self, position_array):
        self.position_array = position_array

    def count(self):
        return len(self.position_array)
