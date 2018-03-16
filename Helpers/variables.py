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
right_sidebar_x = 130
game_message_length = 160 - right_sidebar_x - 2
sidebar_message_log_length = 45

# create a turn number at the start
turn_number = 0

# mouse state
mouse_x = 0
mouse_y = 0