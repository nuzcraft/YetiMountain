# this is the main game loop
import variables as var
from Entity import Entity
from Components.Position import Position
from Components.Glyph import Glyph
from Systems import RenderingSystem
from Helpers.get_input import get_input
from bearlibterminal import terminal

# create the player
player_pos = Position(var.player_array)
player_glyph = Glyph(var.glyph_array)
player = Entity(position=player_pos, glyph=player_glyph, renderable=True)
var.entities.append(player)

# open the terminal, then refresh it to prepare for inputs
terminal.open()
terminal.refresh()

# main game loop, continue until we choose to exit
while var.player_action != 'exit':
    terminal.clear()
    var.player_action = get_input()
    terminal.printf(0, 0, 'Hello, world!')
    RenderingSystem.render_entities()
    terminal.refresh()

# close the terminal to quit the game
terminal.close()
