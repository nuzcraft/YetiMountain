# system for handling blocking entities
import sys
sys.path.append("..")
from Helpers import variables as var
import logging


def is_blocked(x, y):
    # pass in coordinates and return true if the space is blocked
    try:
        for ent in var.entities:
            if ent.position and ent.blocking:
                for x_pos, y_pos in ent.position.position_array:
                    if x_pos == x and y_pos == y:
                        return True
        return False
    except Exception:
        logging.getLogger().error('error in is_blocked', exc_info=True)


def array_is_blocked(position_array):
    # pass in an array and return true if any of the spaces are blocked
    try:
        for ent in var.entities:
            if ent.position and ent.blocking:
                return any(i in position_array for i in ent.position.position_array)
        return False
    except Exception:
        logging.getLogger().error('error in array_is_blocked', exc_info=True)
