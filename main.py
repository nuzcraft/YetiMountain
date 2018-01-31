# this is the main game loop
import variables as var
from Entity import Entity
from Components.Position import Position
from Components.Glyph import Glyph
from Systems import RenderingSystem
from bearlibterminal import terminal

player_pos = Position(var.player_array)
player_glyph = Glyph(var.glyph_array)
player = Entity(position=player_pos, glyph=player_glyph, renderable=True)

var.entities.append(player)

terminal.open()
terminal.printf(0, 0, 'Hello, world!')
RenderingSystem.render_entities()
terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
