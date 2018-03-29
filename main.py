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
import Helpers.action_stack as action_stack
from bearlibterminal import terminal
import logging
from Components.AIs.MoveRandomDirection import MoveRandomDirection

# create the player
player_pos = Position(var.player_array)
player_glyph = Glyph(var.glyph_array, 'white')
player_movement = Movement()
player_input = PlayerInput()
player = Entity(name='player', position=player_pos, glyph=player_glyph, renderable=True, movement=player_movement
                , blocking=True, player_input=player_input, base_speed=1000)
var.entities.append(player)
wall_pos = Position(var.wall_array)
wall_glyph = Glyph(var.wall_glyph, 'grey')
wall = Entity(name='wall', position=wall_pos, glyph=wall_glyph, renderable=True, movement=Movement()
              , blocking=True, ai=MoveRandomDirection(), base_speed=100)
var.entities.append(wall)

# set the name of the file, the logging level, and that we want to truncate each time
logging.basicConfig(filename='ym.log', level=logging.DEBUG,
                    filemode='w')

try:
    # open the terminal, then refresh it to prepare for inputs
    terminal.open()
    var.game_state = 'open'
    logging.getLogger().info('terminal opened')
    terminal.refresh()

    # create the initial action stack
    action_stack.create_initial_stack()
    action_stack.get_action_entities()

    # main game loop, continue until we choose to exit
    while var.player_action != 'exit':
        terminal.clear()
        for ent in var.action_entities:
            if ent.player_input:
                var.player_action, var.mouse_x, var.mouse_y = get_input()
                break
        PlayerInputSystem.handle_input(var.player_action)
        MovementSystem.move_entities()
        AISystem.take_turns()
        # get the next entities in the list from the action stack
        should_get_action_entities = True
        for ent in var.action_entities:
            if ent.player_input and var.player_action == 'none':
                should_get_action_entities = False
        if should_get_action_entities:
            action_stack.get_action_entities()
        RenderingSystem.render_entities()
        RenderingSystem.render_gui()
        terminal.refresh()

    # close the terminal to quit the game
    terminal.close()
    var.game_state = 'closed'
    logging.getLogger().info('terminal closed')
except Exception as e:
    logging.getLogger().error('error in main game loop', exc_info=True)
