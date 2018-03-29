# this section will handle the stack of actions...somehow
import Helpers.variables as var


def create_initial_stack():
    # go to the initial list of entities and create the stack, make sure the player goes first
    for ent in var.entities:
        if ent.player_input:
            var.action_stack.append((ent, 0))
        else:
            var.action_stack.append((ent, ent.speed))


def get_action_entities():
    # go the the action stack and pull the next entities from the list
    # TODO figure out how to speed this up
    var.action_entities.clear()
    lowest_speed = None
    for ent, speed in var.action_stack:
        if lowest_speed is None or speed <= lowest_speed:
            var.action_entities.append(ent)
            lowest_speed = speed
    # take the lowest speed and subtract it from all other speeds in the action stack
    # for everything that made it into action_entities, add it back to the list with the base speed
    for ent, speed in var.action_stack:
        var.action_stack.remove((ent, speed))
        if speed - lowest_speed != 0:
            var.action_stack.append((ent, speed - lowest_speed))
        else:
            var.action_stack.append((ent, ent.speed))



