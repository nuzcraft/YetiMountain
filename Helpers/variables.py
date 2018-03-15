# global variables to be used
player_array = [(10, 10), (10, 11)]
glyph_array = ['@', '/']

wall_array = [(15, 15)]
wall_glyph = ['#']

entities = []

player_action = 'idle'
game_state = 'playing'

# message stuff
game_messages = []
right_sidebar_x = 51
game_message_length = 80 - right_sidebar_x - 2

# create a turn number at the start
turn_number = 0

# mouse state
mouse_x = 0
mouse_y = 0