# class file for an Entity


class Entity:
    # class file for an Entity
    def __init__(self, position=None, glyph=None, renderable=False, movement=None, player_input=None, blocking=False):
        # initialization for self and components
        self.position = position
        self.glyph = glyph
        self.renderable = renderable
        self.movement = movement
        self.player_input = player_input
        self.blocking = blocking
