from cisc108 import assert_equal
from game1_move_upward import *

__VERSION__ = '0.0.1'

################################################################################
## Testing update_world

# Test an initial world
W0 = {'x': 125, 'y': 250, 'direction': 'up'}
update_world(W0)
assert_equal(W0, {'x': 125, 'y': 257, 'direction': 'up'})
update_world(W0)
assert_equal(W0, {'x': 125, 'y': 264, 'direction': 'up'})

# Hitting a wall
W0['x'] = 500
update_world(W0)
assert_equal(W0, {'x': 500, 'y': 271, 'direction': 'up'})
update_world(W0)
assert_equal(W0, {'x': 500, 'y': 278, 'direction': 'up'})