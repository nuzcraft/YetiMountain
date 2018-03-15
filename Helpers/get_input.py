# function to get input from the user
from bearlibterminal import terminal
import Helpers.logger as logger
import logging


def get_input():
    # waits for terminal input, then outputs
    # since we use shift and control for arrow movement,
    # it  needs to be handled separately

    # always return the x and y coordinates of the mouse
    x = terminal.state(terminal.TK_MOUSE_X)
    y = terminal.state(terminal.TK_MOUSE_Y)
    playerinput = 'none'
    if terminal.has_input():
        key = terminal.read()
        if key == terminal.TK_KP_6\
                or key == terminal.TK_L:
            playerinput = 'right'
        elif key == terminal.TK_KP_4\
                or key == terminal.TK_H:
            playerinput = 'left'
        elif key == terminal.TK_KP_8\
                or key == terminal.TK_K\
                or key == terminal.TK_UP:
            playerinput = 'up'
        elif key == terminal.TK_KP_2\
                or key == terminal.TK_J\
                or key == terminal.TK_DOWN:
            playerinput = 'down'
        elif key == terminal.TK_KP_9\
                or key == terminal.TK_U:
            playerinput = 'up-right'
        elif key == terminal.TK_KP_7\
                or key == terminal.TK_Y:
            playerinput = 'up-left'
        elif key == terminal.TK_KP_3\
                or key == terminal.TK_N:
            playerinput = 'down-right'
        elif key == terminal.TK_KP_1\
                or key == terminal.TK_B:
            playerinput = 'down-left'
        elif key == terminal.TK_RIGHT:
            if terminal.check(terminal.TK_SHIFT):
                playerinput = 'up-right'
            elif terminal.check(terminal.TK_CONTROL):
                playerinput = 'down-right'
            else:
                playerinput = 'right'
        elif key == terminal.TK_LEFT:
            if terminal.check(terminal.TK_SHIFT):
                playerinput = 'up-left'
            elif terminal.check(terminal.TK_CONTROL):
                playerinput = 'down-left'
            else:
                playerinput = 'left'
        elif key == terminal.TK_CLOSE\
                or key == terminal.TK_ESCAPE:
            playerinput = 'exit'

        # if there is an imput, we want to log it
        logging.getLogger().debug('player input = ' + playerinput)

    # return the input if nothing, return 'None'
    return playerinput, x, y
