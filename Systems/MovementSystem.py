# system for moving objects
import sys
sys.path.append("..")
from Helpers import variables as var
from Systems import BlockingSystem
import logging
from Helpers.game_message import game_message


def move_entities():
    # loop through entities, looking for ones that need to move
    try:
        for ent in var.entities:
            if ent.movement:
                if ent.movement.direction != 'None':
                    ent.position.direction = ent.movement.direction
                    if ent.speed != 0:
                        interim_pos_array = list(ent.position.position_array)
                        if ent.movement.direction == 'east':
                            # TODO: create a function to move entities a specific number of tiles
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x + 1, y
                        elif ent.movement.direction == 'west':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x - 1, y
                        elif ent.movement.direction == 'north':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x, y - 1
                        elif ent.movement.direction == 'south':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x, y + 1
                        elif ent.movement.direction == 'northeast':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x + 1, y - 1
                        elif ent.movement.direction == 'northwest':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x - 1, y - 1
                        elif ent.movement.direction == 'southeast':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x + 1, y + 1
                        elif ent.movement.direction == 'southwest':
                            for i in range(len(interim_pos_array)):
                                x, y = interim_pos_array[i]
                                interim_pos_array[i] = x - 1, y + 1

                        if not BlockingSystem.array_is_blocked(interim_pos_array, ent):
                            # go ahead and log that we moved
                            game_message(str(var.turn_number) + ' ' + ent.name + ' moved ' + ent.position.direction)
                            logging.getLogger().debug(ent.name + ' moved ' + ent.position.direction)
                            # make the move
                            ent.position.position_array = interim_pos_array
                            # reset movement after moving / may want to change how this works, have default values?
                            ent.movement.direction = 'none'
                            ent.speed = 0

                        else:
                            # we were blocked, log it and return
                            game_message(str(var.turn_number) + ' ' + ent.name + ' blocked')
                            logging.getLogger().debug(ent.name + ' blocked')
                            ent.movement.direction = 'none'
                            ent.speed = 0
                            return
    except Exception:
        logging.getLogger().error('error in move_entities', exc_info=True)

