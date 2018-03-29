# function(s) for handling player input
from bearlibterminal import terminal
import sys
sys.path.append("..")
from Helpers import variables as var
import logging


def handle_input(input_string):
    # input is a string, this is then applied to all objects that have a 'player_input' component
    # but only if the command is meant for entities. UI commands are handled separately
    try:
        if input_string == 'page up' or input_string == 'page down' or input_string == 'mouse wheel scroll':
            apply_ui_inputs(input_string)
        for ent in var.action_entities:  # 3/28 switched from var.entities to var.action_entities
            if ent.player_input and ent.player_input.action != input_string:
                ent.player_input.action = input_string
        apply_inputs()
    except Exception:
        logging.getLogger().error('error in handle_input', exc_info=True)


def apply_inputs():
    # uses the player_input component and applies it to movement
    try:
        for ent in var.action_entities:
            if ent.player_input and ent.movement:
                if ent.player_input.action == 'none':
                    ent.movement.direction = ent.player_input.action
                    ent.movement.speed = 0
                else:
                    ent.movement.speed = 100
                    if ent.player_input.action == 'right':
                        ent.movement.direction = 'east'
                    elif ent.player_input.action == 'left':
                        ent.movement.direction = 'west'
                    elif ent.player_input.action == 'up':
                        ent.movement.direction = 'north'
                    elif ent.player_input.action == 'down':
                        ent.movement.direction = 'south'
                    elif ent.player_input.action == 'up-right':
                        ent.movement.direction = 'northeast'
                    elif ent.player_input.action == 'down-right':
                        ent.movement.direction = 'southeast'
                    elif ent.player_input.action == 'up-left':
                        ent.movement.direction = 'northwest'
                    elif ent.player_input.action == 'down-left':
                        ent.movement.direction = 'southwest'
                    else:
                        ent.player_input.action = 'none'
                        ent.movement.speed = 0
                # if the player did something, increase the turn number
                if ent.player_input.action != 'none':
                    var.turn_number += 1

    except Exception:
        logging.getLogger().error('error in apply_inputs', exc_info=True)


def apply_ui_inputs(input_string):
    # this will take inputs that apply to the ui and apply them
    if input_string == 'mouse wheel scroll':
        scroll_amount = terminal.state(terminal.TK_MOUSE_WHEEL)
        if scroll_amount <= 0:
            if len(var.message_log) - var.message_log_scroll_index > var.message_log_height - 2 \
                    and len(var.message_log) >= var.message_log_height - 2:
                var.message_log_scroll_index += 1
        else:
            if len(var.message_log) >= var.message_log_height - 2 \
                    and var.message_log_scroll_index > 0:
                var.message_log_scroll_index -= 1
    if input_string == 'page up':
        if len(var.message_log) - var.message_log_scroll_index > var.message_log_height-2\
                and len(var.message_log) >= var.message_log_height - 2:
            var.message_log_scroll_index += 1
    elif input_string == 'page down':
        if len(var.message_log) >= var.message_log_height - 2\
                and var.message_log_scroll_index > 0:
            var.message_log_scroll_index -= 1

