# system for moving objects
import sys
sys.path.append("..")
import variables as var
from Systems import BlockingSystem


def move_entities():
    # loop through entities, looking for ones that need to move
    for ent in var.entities:
        if ent.movement:
            if ent.movement.direction != 'None':
                ent.position.direction = ent.movement.direction
                if ent.movement.speed != 0:
                    interim_pos_array = list(ent.position.position_array)
                    if ent.movement.direction == 'east':
                        # TODO: create a function to move entities a specific number of tiles
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x + 1, y
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'west':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x - 1, y
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'north':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x, y - 1
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'south':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x, y + 1
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'northeast':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x + 1, y - 1
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'northwest':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x - 1, y - 1
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'southeast':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x + 1, y + 1
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    elif ent.movement.direction == 'southwest':
                        for i in range(len(interim_pos_array)):
                            x, y = interim_pos_array[i]
                            interim_pos_array[i] = x - 1, y + 1
                        if BlockingSystem.array_is_blocked(interim_pos_array):
                            return
                    ent.position.position_array = interim_pos_array

