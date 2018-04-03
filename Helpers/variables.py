# window variables (3/27/2018 cut window in half to use bigger tiles)
window_length = 80
window_height = 30

# global variables to be used
player_array = [(10, 10), (10, 11)]
glyph_array = ['@', '/']

wall_array = [(15, 15)]
wall_glyph = ['#']

entities = []
entity_action_list = []
active_entities = []

player_action = 'idle'
game_state = 'closed'

# message stuff
message_log = []
message_log_scroll_index = 0

# create a turn number at the start
turn_number = 0

# mouse state
mouse_x = 0
mouse_y = 0

# characters
# single pipe
c_pipe_vertical = '[0x2502]'
c_pipe_horizontal = '[0x2500]'
c_pipe_down_right_corner = '[0x250C]'
c_pipe_down_left_corner = '[0x2510]'
c_pipe_up_right_corner = '[0x2514]'
c_pipe_up_left_corner = '[0x2518]'

# double pipe
c_dblpipe_vertical = '[0x2551]'
c_dblpipe_horizontal = '[0x2550]'
c_dblpipe_down_right_corner = '[0x2554]'
c_dblpipe_down_left_corner = '[0x2557]'
c_dblpipe_up_right_corner = '[0x255A]'
c_dblpipe_up_left_corner = '[0x255D]'

# message log gui
message_log_width = 30
message_log_height = 15
message_log_x = window_length - message_log_width
message_log_y = window_height - message_log_height

# status gui
status_width = message_log_width
status_height = window_height - message_log_height
status_x = window_length - status_width
status_y = 0

