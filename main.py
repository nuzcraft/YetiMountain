# this is the main game loop
from Helpers import variables as var
from Components.Entity import Entity
from Components.Position import Position
from Components.Glyph import Glyph
from Components.Movement import Movement
from Components.PlayerInput import PlayerInput
from Systems import RenderingSystem
from Systems import PlayerInputSystem
from Systems import MovementSystem
from Systems import AISystem
from Helpers.get_input import get_input
from Helpers.get_active_entities import get_active_entities
from bearlibterminal import terminal
import logging
from Components.AIs.MoveRandomDirection import MoveRandomDirection

# create the player
player_pos = Position(var.player_array)
player_glyph = Glyph(var.glyph_array, 'white')
player_movement = Movement()
player_input = PlayerInput()
player = Entity(name='player', position=player_pos, glyph=player_glyph, renderable=True, movement=player_movement
                , blocking=True, player_input=player_input, base_speed=100)
var.entities.append(player)
wall_pos = Position(var.wall_array)
wall_glyph = Glyph(var.wall_glyph, 'grey')
wall = Entity(name='wall', position=wall_pos, glyph=wall_glyph, renderable=True, movement=Movement()
              , blocking=True, ai=MoveRandomDirection(), base_speed=100)
var.entities.append(wall)
var.active_entities.append(player)

# set the name of the file, the logging level, and that we want to truncate each time
logging.basicConfig(filename='ym.log', level=logging.DEBUG,
                    filemode='w')

try:
    # open the terminal, then refresh it to prepare for inputs
    terminal.open()
    var.game_state = 'open'
    logging.getLogger().info('terminal opened')
    terminal.refresh()
    var.game_state = 'playing'
    logging.getLogger().info('game_state=playing')

    # main game loop, continue until we choose to exit
    while var.player_action != 'exit':
        terminal.clear()
        var.player_action, var.mouse_x, var.mouse_y = get_input()
        PlayerInputSystem.handle_input(var.player_action)
        if not var.game_state == 'waiting':
            MovementSystem.move_entities()
            AISystem.take_turns()
            # get entities from the action_list and add them to the active_entities list
            get_active_entities()
        RenderingSystem.render_entities()
        RenderingSystem.render_gui()
        terminal.refresh()

    # close the terminal to quit the game
    terminal.close()
    var.game_state = 'closed'
    logging.getLogger().info('terminal closed')
except Exception as e:
    logging.getLogger().error('error in main game loop', exc_info=True)
