# This is the rendering system that will be used to render entities
import sys
sys.path.append("..")
import variables as var
from bearlibterminal import terminal


def render_entities():
    # this function will render all entities that are renderable,
    # have a position, and have a glyph
    for ent in var.entities:
        if ent.renderable and ent.position and ent.glyph:
            for i in range(len(ent.position.position_array)):
                x, y = ent.position.position_array[i]
                g = ent.glyph.glyph_array[i]
                terminal.printf(x, y, g)
