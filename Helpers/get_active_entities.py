# this file will get active entities from the entity action list
import variables as var


def get_active_entities():
    # looks at the action list and pulls all entities with the lowest turn timer
    var.active_entities = []
    lowest_turn_timer = None
    # get the lowest turn_timer in the action list
    for ent in var.entity_action_list:
        if lowest_turn_timer is None:
            lowest_turn_timer = ent.turn_timer
        elif ent.turn_timer < lowest_turn_timer:
            lowest_turn_timer = ent.turn_timer
    # add all entities with this turn timer to active_entities
    # remove them from entity action list
    # decrease the turn timer of other entities in the action list by the lowest turn timer amount
    for ent in var.entity_action_list:
        if ent.turn_timer == lowest_turn_timer:
            var.active_entities.append(ent)
            var.entity_action_list.remove(ent)
        else:
            ent.turn_timer -= lowest_turn_timer

