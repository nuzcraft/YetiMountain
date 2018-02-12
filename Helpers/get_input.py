# function to get input from the user
from bearlibterminal import terminal


def get_input():
    # waits for terminal input, then outputs
    # since we use shift and control for arrow movement,
    # it  needs to be handled separately

    # always return the x and y coordinates of the mouse
    x = terminal.state(terminal.TK_MOUSE_X)
    y = terminal.state(terminal.TK_MOUSE_Y)
    if terminal.has_input():
        key = terminal.read()
        if key == terminal.TK_KP_6\
                or key == terminal.TK_L:
            return 'right', x, y
        elif key == terminal.TK_KP_4\
                or key == terminal.TK_H:
            return 'left', x, y
        elif key == terminal.TK_KP_8\
                or key == terminal.TK_K\
                or key == terminal.TK_UP:
            return 'up', x, y
        elif key == terminal.TK_KP_2\
                or key == terminal.TK_J\
                or key == terminal.TK_DOWN:
            return 'down', x, y
        elif key == terminal.TK_KP_9\
                or key == terminal.TK_U:
            return 'up-right', x, y
        elif key == terminal.TK_KP_7\
                or key == terminal.TK_Y:
            return 'up-left', x, y
        elif key == terminal.TK_KP_3\
                or key == terminal.TK_N:
            return 'down-right', x, y
        elif key == terminal.TK_KP_1\
                or key == terminal.TK_B:
            return 'down-left', x, y
        elif key == terminal.TK_RIGHT:
            if terminal.check(terminal.TK_SHIFT):
                return 'up-right', x, y
            elif terminal.check(terminal.TK_CONTROL):
                return 'down-right', x, y
            return 'right', x, y
        elif key == terminal.TK_LEFT:
            if terminal.check(terminal.TK_SHIFT):
                return 'up-left', x, y
            elif terminal.check(terminal.TK_CONTROL):
                return 'down-left', x, y
            return 'left', x, y
        elif key == terminal.TK_CLOSE\
                or key == terminal.TK_ESCAPE:
            return 'exit', x, y

    # if nothing, return 'None'
    return 'None', x, y
