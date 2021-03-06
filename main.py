# this is the main game loop
import variables as var
from Entity import Entity
from Components.Position import Position
from Components.Glyph import Glyph
from Components.Movement import Movement
from Components.PlayerInput import PlayerInput
from Systems import RenderingSystem
from Systems import PlayerInputSystem
from Systems import MovementSystem
from Helpers.get_input import get_input
from bearlibterminal import terminal

# create the player
player_pos = Position(var.player_array)
player_glyph = Glyph(var.glyph_array)
player_movement = Movement()
player_input = PlayerInput()
player = Entity(position=player_pos, glyph=player_glyph, renderable=True, movement=player_movement
                , player_input=player_input)
var.entities.append(player)
wall_pos = Position(var.wall_array)
wall_glyph = Glyph(var.wall_glyph)
wall = Entity(position=wall_pos, glyph=wall_glyph, renderable=True, blocking=True)
var.entities.append(wall)

# open the terminal, then refresh it to prepare for inputs
terminal.open()
terminal.refresh()

# main game loop, continue until we choose to exit
while var.player_action != 'exit':
    terminal.clear()
    var.player_action, var.mouse_x, var.mouse_y = get_input()
    PlayerInputSystem.handle_input(var.player_action)
    MovementSystem.move_entities()
    terminal.printf(0, 0, 'Hello, world!')
    RenderingSystem.render_entities()
    terminal.refresh()

# close the terminal to quit the game
terminal.close()
