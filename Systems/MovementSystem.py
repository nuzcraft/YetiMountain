# system for moving objects
import sys
sys.path.append("..")
import variables as var


def move_entities():
    # loop through entities, looking for ones that need to move
    for ent in var.entities:
        if ent.movement:
            if ent.movement.direction != 'None':
                ent.position.direction = ent.movement.direction
                if ent.movement.speed != 0:
                    if ent.movement.direction == 'east':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x + 1, y
                    elif ent.movement.direction == 'west':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x - 1, y
                    elif ent.movement.direction == 'north':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x, y - 1
                    elif ent.movement.direction == 'south':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x, y + 1
                    elif ent.movement.direction == 'northeast':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x + 1, y - 1
                    elif ent.movement.direction == 'northwest':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x - 1, y - 1
                    elif ent.movement.direction == 'southeast':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x + 1, y + 1
                    elif ent.movement.direction == 'southwest':
                        for i in range(len(ent.position.position_array)):
                            x, y = ent.position.position_array[i]
                            ent.position.position_array[i] = x - 1, y + 1

