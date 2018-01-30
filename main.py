# this is the main game loop
import variables as var
from Entity import Entity
from Components.Position import Position
from bearlibterminal import terminal

player_pos = Position(var.player_array)
player = Entity(position=player_pos, character=var.character_array)

terminal.open()
terminal.printf(0, 0, 'Hello, world!')
# terminal.printf(player.position.x, player.position.y, '@')
for i in range(player.position.count()):
    x, y = player.position.position_array(i)
    c = player.character.character_array(i)
    terminal.printf(x, y, c)

terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
