# this is the main game loop

from bearlibterminal import terminal

terminal.open()
terminal.printf(0, 0, 'Hello, world!')
terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()