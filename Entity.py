# class file for an Entity


class Entity:
    # class file for an Entity
    def __init__(self, position=None, glyph=None, renderable=False):
        # initialization for self and components
        self.position = position
        self.glyph = glyph
        self.renderable = renderable
