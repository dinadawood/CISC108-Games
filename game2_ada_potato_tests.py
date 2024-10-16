from cisc108 import assert_equal
from game2_ada_potato import *

__VERSION__ = '0.0.1'

################################################################################
## Testing switch_mode
W0 = { 'mode': 'ada', 'timer': 30, 'score': 0 }
switch_mode(W0)
assert_equal(W0, {'mode': 'potato', 'timer': 30, 'score': 0})
switch_mode(W0)
assert_equal(W0, {'mode': 'ada', 'timer': 30, 'score': 0})

# Switches regardless of timer status
W1 = { 'mode': 'potato', 'timer': 0, 'score': 0 }
switch_mode(W1)
assert_equal(W1, {'mode': 'ada', 'timer': 0, 'score': 0})
switch_mode(W1)
assert_equal(W1, {'mode': 'potato', 'timer': 0, 'score': 0})

################################################################################
## Testing update_world

# Test an initial world
W0 = { 'mode': 'ada', 'timer': 30, 'score': 0 }
update_world(W0)
assert_equal(W0, {'mode': 'ada', 'timer': 29, 'score': 0})
update_world(W0)
assert_equal(W0, {'mode': 'ada', 'timer': 28, 'score': 0})

# Fast forward to 0 steps switches to Potato
W0['timer'] = 0
update_world(W0)
assert_equal(W0, {'mode': 'potato', 'timer': 60, 'score': 0})
update_world(W0)
assert_equal(W0, {'mode': 'potato', 'timer': 59, 'score': 0})

# Fast forward to 0 steps switches back to Ada
W0['timer'] = 0
update_world(W0)
assert_equal(W0, {'mode': 'ada', 'timer': 60, 'score': 0})
update_world(W0)
assert_equal(W0, {'mode': 'ada', 'timer': 59, 'score': 0})

################################################################################
## Testing handle_mouse

# Clicking Ada increases the score
W1 = { 'mode': 'ada', 'timer': 0, 'score': 0 }
handle_mouse(W1, 250, 250, 'left')
assert_equal(W1, {'mode': 'ada', 'timer': 0, 'score': 1})
handle_mouse(W1, 250, 250, 'left')
assert_equal(W1, {'mode': 'ada', 'timer': 0, 'score': 2})

# Clicking Potato decreases the score
W1['mode'] = 'potato'
handle_mouse(W1, 250, 250, 'left')
assert_equal(W1, {'mode': 'potato', 'timer': 0, 'score': 1})
handle_mouse(W1, 250, 250, 'left')
assert_equal(W1, {'mode': 'potato', 'timer': 0, 'score': 0})