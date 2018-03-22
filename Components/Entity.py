# class file for an Entity


class Entity:
    # class file for an Entity
    def __init__(self, name, position=None, glyph=None, renderable=False, movement=None, player_input=None
                 , blocking=False, ai=None):
        # initialization for self and components
        self.name = name
        self.position = position
        self.glyph = glyph
        self.renderable = renderable
        self.movement = movement
        self.player_input = player_input
        self.blocking = blocking
        self.ai = ai
        if self.ai:
            self.ai.owner = self
