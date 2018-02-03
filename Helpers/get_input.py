# function to get input from the user
from bearlibterminal import terminal


def get_input():
    # waits for terminal input, then outputs
    if terminal.has_input():
        key = terminal.read()
        if key == terminal.TK_RIGHT:
            return 'right'
        elif key == terminal.TK_LEFT:
            return 'left'
        elif key == terminal.TK_UP:
            return 'up'
        elif key == terminal.TK_DOWN:
            return 'down'
        elif key == terminal.TK_CLOSE:
            return 'exit'

    # if nothing, return 'None'
    return 'None'
