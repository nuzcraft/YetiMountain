# function to get input from the user
from bearlibterminal import terminal


def get_input():
    # waits for terminal input, then outputs
    if terminal.has_input():
        key = terminal.read()
        if key == terminal.TK_CLOSE:
            return 'exit'
