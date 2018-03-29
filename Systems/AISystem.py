# this is the system meant to handle AIs
import logging
import Helpers.variables as var


def take_turns():
    try:
        # let the ai take turns if the player has taken their turn
        player_input = False
        for ent in var.action_entities:
            if ent.player_input:
                player_input = True
        if player_input is False or (var.player_action != 'none' and var.player_action != 'page up' and
                                     var.player_action != 'page down' and var.player_action != 'mouse wheel scroll'):
            for ent in var.action_entities:
                if ent.ai:
                    ent.ai.take_turn()

    except Exception:
        logging.GetLogger().error('error in take_turn', exc_info=True)