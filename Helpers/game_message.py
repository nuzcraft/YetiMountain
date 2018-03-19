# this function takes a string and converts it into game messages
import textwrap
import Helpers.variables as var
import logging


def game_message(message, color='white'):
    # take the message, wrap the text if necessary, and append it to game_messages
    try:
        # use (message_log_length - 2) to put it inside the borders of the message log
        new_message_lines = textwrap.wrap(message, var.message_log_width - 2)
        for line in new_message_lines:
            var.message_log.append((line, color))
    except Exception:
        logging.getLogger().error('error in game_message', exc_info=True)
