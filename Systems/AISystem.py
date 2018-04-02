# this is the system meant to handle AIs
import logging
import Helpers.variables as var


def take_turns():
    try:
        # let the ai take turns if the player has taken their turn
        if var.player_action != 'none' and var.player_action != 'page up' and var.player_action != 'page down' and \
                var.player_action != 'mouse wheel scroll':
            for ent in var.entities:
                if ent.ai:
                    ent.ai.take_turn()
    except Exception:
        logging.GetLogger().error('error in take_turn', exc_info=True)