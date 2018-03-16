# This is the rendering system that will be used to render entities
import sys
sys.path.append("..")
from Helpers import variables as var
from bearlibterminal import terminal
import logging


def render_entities():
    # this function will render all entities that are renderable,
    # have a position, and have a glyph
    try:
        for ent in var.entities:
            if ent.renderable and ent.position and ent.glyph:
                for i in range(len(ent.position.position_array)):
                    x, y = ent.position.position_array[i]
                    g = ent.glyph.glyph_array[i]
                    terminal.printf(x*2, y, '[font=map]'+g+'[/font]', terminal.color(terminal.color_from_name(ent.glyph.color)))
    except Exception:
        logging.GetLogger().error('error in render_entities', exc_info=True)


def render_game_messages():
    # this function will render game messages, by flipping the list, and rendering from the bottom
    try:
        y = 59
        reversed_game_messages = reversed(var.game_messages)
        for (line, color) in reversed_game_messages:
            terminal.printf(var.right_sidebar_x + 1, y, line,
                            terminal.color(terminal.color_from_name(color)))
            y -= 1
            if y - var.sidebar_message_log_length <= 0:
                break
    except Exception:
        logging.getLogger().error('error in render_game_messages', exc_info=True)


def render_gui():
    # this will render the outlines of the gui
    try:
        # first, render the vertical pipes around the game log
        # for the length of the message log, print vertical pipes on the right and left edges
        for x in range(var.sidebar_message_log_length):
            terminal.printf(var.right_sidebar_x, 59-x, '[0xE000]')
    except Exception:
        logging.getLogger().error('error in render_gui', exc_info=True)

