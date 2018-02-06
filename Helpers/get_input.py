# function to get input from the user
from bearlibterminal import terminal


def get_input():
    # waits for terminal input, then outputs
    # since we use shift and control for arrow movement,
    # it  needs to be handled separately
    if terminal.has_input():
        key = terminal.read()
        if key == terminal.TK_KP_6\
                or key == terminal.TK_L:
            return 'right'
        elif key == terminal.TK_KP_4\
                or key == terminal.TK_H:
            return 'left'
        elif key == terminal.TK_KP_8\
                or key == terminal.TK_K\
                or key == terminal.TK_UP:
            return 'up'
        elif key == terminal.TK_KP_2\
                or key == terminal.TK_J\
                or key == terminal.TK_DOWN:
            return 'down'
        elif key == terminal.TK_KP_9\
                or key == terminal.TK_U:
            return 'up-right'
        elif key == terminal.TK_KP_7\
                or key == terminal.TK_Y:
            return 'up-left'
        elif key == terminal.TK_KP_3\
                or key == terminal.TK_N:
            return 'down-right'
        elif key == terminal.TK_KP_1\
                or key == terminal.TK_B:
            return 'down-left'
        elif key == terminal.TK_RIGHT:
            if terminal.check(terminal.TK_SHIFT):
                return 'up-right'
            elif terminal.check(terminal.TK_CONTROL):
                return 'down-right'
            return 'right'
        elif key == terminal.TK_LEFT:
            if terminal.check(terminal.TK_SHIFT):
                return 'up-left'
            elif terminal.check(terminal.TK_CONTROL):
                return 'down-left'
            return 'left'
        elif key == terminal.TK_CLOSE\
                or key == terminal.TK_ESCAPE:
            return 'exit'

    # if nothing, return 'None'
    return 'None'
