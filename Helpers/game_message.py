# this function takes a string and converts it into game messages
import textwrap
import Helpers.variables as var
import logging


def game_message(message, color = 'white'):
    # take the message, wrap the text if necessary, and append it to game_messages
    try:
        new_message_lines = textwrap.wrap(message, var.game_message_length)
        for line in new_message_lines:
            var.game_messages.append((line, color))
    except Exception:
        logging.getLogger().error('error in game_message', exc_info=True)
