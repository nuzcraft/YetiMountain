# window variables
window_length = 160
window_height = 60

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

# create a turn number at the start
turn_number = 0

# mouse state
mouse_x = 0
mouse_y = 0

# characters
c_vertical_pipe = '[0x2502]'
c_horizontal_pipe = '[0x2500]'
c_down_right_pipe_corner = '[0x250C]'
c_down_left_pipe_corner = '[0x2510]'
c_up_right_pipe_corner = '[0x2514]'
c_up_left_pipe_corner = '[0x2518]'

message_log_width = 30
message_log_height = 45
message_log_x = window_length - message_log_width - 1
message_log_y = window_height - message_log_height - 1

