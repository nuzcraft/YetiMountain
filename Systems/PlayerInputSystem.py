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
        for ent in var.active_entities:
            if ent.player_input:
                # if there's a player controlled character in the list, change game_state to waiting
                # TODO: this assumes every player controlled character in the action_entities list will take the same
                # command
                var.game_state = 'waiting'
                if ent.player_input.action != input_string:
                    ent.player_input.action = input_string
        apply_inputs()
    except Exception:
        logging.getLogger().error('error in handle_input', exc_info=True)


def apply_inputs():
    # uses the player_input component and applies it to movement
    try:
        for ent in var.active_entities:  # entities:
            if ent.player_input and ent.movement:
                if ent.player_input.action == 'none':
                    ent.movement.direction = ent.player_input.action
                    ent.speed = 0
                    ent.turn_timer = 0
                else:
                    ent.speed = 100
                    ent.turn_timer = 100
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
                        ent.speed = 0
                        ent.turn_timer = 0
                # if the player did something, add them to the entity action list, and increase the turn number
                if ent.player_input.action != 'none':
                    var.entity_action_list.append(ent)
                    var.turn_number += 1
                    var.game_state = 'playing'
                    logging.getLogger().debug('game_state=playing')

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

