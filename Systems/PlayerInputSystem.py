# function(s) for handling player input
import sys
sys.path.append("..")
import variables as var


def handle_input(input_string):
    # input is a string, this is then applied to all objects that have a 'player_input' component
    for ent in var.entities:
        if ent.player_input and ent.player_input.action != input_string:
            ent.player_input.action = input_string
    apply_inputs()


def apply_inputs():
    # uses the player_input component and applies it to movement
    for ent in var.entities:
        if ent.player_input and ent.movement:
            if ent.player_input.action == 'None':
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
                else:
                    ent.player_input.action = 'None'
                    ent.movement.speed = 0

