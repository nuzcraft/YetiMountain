# this is the main game loop
import variables as var
from Entity import Entity
from Components.Position import Position
from Components.Glyph import Glyph
from bearlibterminal import terminal

player_pos = Position(var.player_array)
player_glyph = Glyph(var.glyph_array)
player = Entity(position=player_pos, character=player_glyph)

terminal.open()
terminal.printf(0, 0, 'Hello, world!')
# terminal.printf(player.position.x, player.position.y, '@')
for i in range(len(player.position.position_array)):
    x, y = player.position.position_array[i]
    g = player.character.glyph_array[i]
    terminal.printf(x, y, g)

terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
