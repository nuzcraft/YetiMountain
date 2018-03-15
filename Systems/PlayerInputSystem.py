# function(s) for handling player input
import sys
sys.path.append("..")
from Helpers import variables as var
import logging


def handle_input(input_string):
    # input is a string, this is then applied to all objects that have a 'player_input' component
    try:
        for ent in var.entities:
            if ent.player_input and ent.player_input.action != input_string:
                ent.player_input.action = input_string
        apply_inputs()
    except Exception:
        logging.getLogger().error('error in handle_input', exc_info=True)


def apply_inputs():
    # uses the player_input component and applies it to movement
    try:
        for ent in var.entities:
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
    except Exception:
        logging.getLogger().error('error in apply_inputs', exc_info=True)
