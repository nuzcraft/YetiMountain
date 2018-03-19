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
        msg_log_scroll_index = var.message_log_scroll_index
        reversed_game_messages = reversed(var.message_log)
        for (line, color) in reversed_game_messages:
            if msg_log_scroll_index > 0:
                msg_log_scroll_index -= 1
            else:
                terminal.printf(var.message_log_x + 1, y, line,
                                terminal.color(terminal.color_from_name(color)))
                y -= 1
                num_messages += 1
                if num_messages >= var.message_log_height - 2:  # -2 to remove the top and bottom
                    break
    except Exception:
        logging.getLogger().error('error in render_game_messages', exc_info=True)


def render_gui():
    # this will render the outlines of the gui
    try:
        # message log section
        render_gui_rectangle(var.message_log_x, var.message_log_y, var.message_log_width, var.message_log_height
                             , color='white', style='single pipe')
        # status section
        render_gui_rectangle(var.status_x, var.status_y, var.status_width, var.status_height, color='white'
                             , style='single pipe')
        # render game messages
        render_game_messages()

    except Exception:
        logging.getLogger().error('error in render_gui', exc_info=True)


def render_gui_rectangle(top_left_x, top_left_y, width, height, color='white', style='single pipe'):
    # this will render a rectangle on the screen
    # inputs: top_left_x, top_left_y, width, height, color, style
    # style can be 'single pipe' or 'double pipe'
    try:

        horizontal = var.c_pipe_horizontal
        vertical = var.c_pipe_vertical
        dr_corner = var.c_pipe_down_right_corner
        dl_corner = var.c_pipe_down_left_corner
        ur_corner = var.c_pipe_up_right_corner
        ul_corner = var.c_pipe_up_left_corner
        if style == 'double pipe':
            horizontal = var.c_dblpipe_horizontal
            vertical = var.c_dblpipe_vertical
            dr_corner = var.c_dblpipe_down_right_corner
            dl_corner = var.c_dblpipe_down_left_corner
            ur_corner = var.c_dblpipe_up_right_corner
            ul_corner = var.c_dblpipe_up_left_corner

        # print vertical pipes on the right and left edges
        for y in range(height - 2): # -2 removes the top and bottom
            terminal.printf(top_left_x, top_left_y + y + 1, vertical
                            , terminal.color(terminal.color_from_name(color)))
            terminal.printf(top_left_x + width - 1, top_left_y + y + 1, vertical
                            , terminal.color(terminal.color_from_name(color)))
        # horizontal bars for the top and bottom
        for x in range(width - 2): # -2 removes the left and right
            terminal.printf(top_left_x + x + 1, top_left_y, horizontal
                            , terminal.color(terminal.color_from_name(color)))
            terminal.printf(top_left_x + x + 1, top_left_y + height - 1, horizontal
                            , terminal.color(terminal.color_from_name(color)))
        # corners!!
        terminal.printf(top_left_x, top_left_y, dr_corner
                        , terminal.color(terminal.color_from_name(color)))
        terminal.printf(top_left_x + width - 1, top_left_y, dl_corner
                        , terminal.color(terminal.color_from_name(color)))
        terminal.printf(top_left_x, top_left_y + height - 1, ur_corner
                        , terminal.color(terminal.color_from_name(color)))
        terminal.printf(top_left_x + width - 1, top_left_y + height - 1, ul_corner
                        , terminal.color(terminal.color_from_name(color)))
    except Exception:
        logging.get_logger().error('error in render_gui_rectangle', exc_info=True)

