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
        y = var.window_height - 2
        num_messages = 0
        reversed_game_messages = reversed(var.game_messages)
        for (line, color) in reversed_game_messages:
            terminal.printf(var.message_log_x + 1, y, line,
                            terminal.color(terminal.color_from_name(color)))
            y -= 1
            num_messages += 1
            if num_messages >= var.message_log_height:
                break
    except Exception:
        logging.getLogger().error('error in render_game_messages', exc_info=True)


def render_gui():
    # this will render the outlines of the gui
    try:
        # message log section
        # TODO: Turn this into its own function render_gui_rectangle
        # print vertical pipes on the right and left edges
        for y in range(var.message_log_height - 1):
            terminal.printf(var.message_log_x, var.message_log_y + y + 1, var.c_vertical_pipe
                            , terminal.color(terminal.color_from_name('white')))
            terminal.printf(var.message_log_x + var.message_log_width, var.message_log_y + y + 1, var.c_vertical_pipe
                            , terminal.color(terminal.color_from_name('white')))
        # horizontal bars for the top and bottom
        for x in range(var.message_log_width - 1):
            terminal.printf(var.message_log_x + x + 1, var.message_log_y, var.c_horizontal_pipe
                            , terminal.color(terminal.color_from_name('white')))
            terminal.printf(var.message_log_x + x + 1, var.message_log_y + var.message_log_height, var.c_horizontal_pipe
                            , terminal.color(terminal.color_from_name('white')))
        # corners!!
        terminal.printf(var.message_log_x, var.message_log_y, var.c_down_right_pipe_corner
                        , terminal.color(terminal.color_from_name('white')))
        terminal.printf(var.message_log_x + var.message_log_width, var.message_log_y, var.c_down_left_pipe_corner
                        , terminal.color(terminal.color_from_name('white')))
        terminal.printf(var.message_log_x, var.message_log_y + var.message_log_height, var.c_up_right_pipe_corner
                        , terminal.color(terminal.color_from_name('white')))
        terminal.printf(var.message_log_x + var.message_log_width, var.message_log_y + var.message_log_height, var.c_up_left_pipe_corner
                        , terminal.color(terminal.color_from_name('white')))

    except Exception:
        logging.getLogger().error('error in render_gui', exc_info=True)

