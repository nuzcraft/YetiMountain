# class file for displayed characters


class Glyph:
    # define the character component of an entity
    def __init__(self, glyph_array, color):
        self.glyph_array = glyph_array
        # at the moment, keep this a solid color; will probably become an array soon
        self.color = color

