from cisc108 import assert_equal
from game3_red_dot import *

__VERSION__ = '0.0.1'

################################################################################
## Testing random_value
# Testing random functions is hard! Three strategies: assert that it produces
# values within a range, generate many tests programmatically, and unit test
# based on a seed to make it deterministic (predictable). But we don't expect
# much from tests on random functions. Isolate the randomness to a helper
# function, and focus on testing the rest of the behavior.

random.seed(0)

for i in range(4):
    point = make_random_position()
    # Test the function produces values in the expected range
    assert_equal(0 <= point['x'] <= WINDOW_WIDTH, True)
    assert_equal(0 <= point['y'] <= WINDOW_HEIGHT, True)
    
################################################################################
## Testing make_red_dot

for i in range(4):
    dot = make_red_dot()
    # Test the function produces values in the expected range
    assert_equal(0 <= dot['current']['x'] <= WINDOW_WIDTH, True)
    assert_equal(0 <= dot['current']['y'] <= WINDOW_HEIGHT, True)
    assert_equal(0 <= dot['goal']['x'] <= WINDOW_WIDTH, True)
    assert_equal(0 <= dot['goal']['y'] <= WINDOW_HEIGHT, True)
    # Test the function has different current and goal (unlikely)
    assert_equal(dot['current'] != dot['goal'], True)

################################################################################
## Testing angle_between
ORIGIN = {'x': 0, 'y': 0}
TOP_RIGHT = {'x': WINDOW_WIDTH, 'y': WINDOW_HEIGHT}
TOP_LEFT = {'x': 0, 'y': WINDOW_HEIGHT}
BOTTOM_RIGHT = {'x': WINDOW_WIDTH, 'y': 0}
CENTER = {'x': WINDOW_WIDTH/2, 'y': WINDOW_HEIGHT/2}
CENTER_LEFT = {'x': 0, 'y': WINDOW_HEIGHT/2}
CENTER_RIGHT = {'x': WINDOW_WIDTH, 'y': WINDOW_HEIGHT/2}
CENTER_BOTTOM = {'x': WINDOW_WIDTH/2, 'y': 0}
CENTER_TOP = {'x': WINDOW_WIDTH/2, 'y': WINDOW_HEIGHT}
assert_equal(angle_between(CENTER, TOP_RIGHT), math.pi/4)
assert_equal(angle_between(CENTER, CENTER_TOP), math.pi/2)
assert_equal(angle_between(CENTER, TOP_LEFT), 3*math.pi/4)
assert_equal(angle_between(CENTER, CENTER_LEFT), math.pi)
assert_equal(angle_between(CENTER, ORIGIN), -3*math.pi/4)
assert_equal(angle_between(CENTER, CENTER_BOTTOM), -math.pi/2)
assert_equal(angle_between(CENTER, BOTTOM_RIGHT), -math.pi/4)
assert_equal(angle_between(CENTER, CENTER_RIGHT), 0.0)

################################################################################
## Testing distance_between
# Cardinal directions from center
assert_equal(distance_between(CENTER, TOP_RIGHT), math.sqrt(125000))
assert_equal(distance_between(CENTER, CENTER_TOP), 250.0)
assert_equal(distance_between(CENTER, TOP_LEFT), math.sqrt(125000))
assert_equal(distance_between(CENTER, CENTER_LEFT), 250.0)
assert_equal(distance_between(CENTER, ORIGIN), math.sqrt(125000))
assert_equal(distance_between(CENTER, CENTER_BOTTOM), 250.0)
assert_equal(distance_between(CENTER, BOTTOM_RIGHT), math.sqrt(125000))
assert_equal(distance_between(CENTER, CENTER_RIGHT), 250.0)
# And also some weirder angles
assert_equal(distance_between(CENTER_LEFT, BOTTOM_RIGHT), math.sqrt(312500))
assert_equal(distance_between(ORIGIN, TOP_RIGHT), math.sqrt(500000))
# And a classic Pythagorean Triple
assert_equal(distance_between(ORIGIN, {'x': 3, 'y': 4}), 5.0)

################################################################################
## Testing x_from_angle_speed
assert_equal(x_from_angle_speed(0, 5), 5.0)
assert_equal(x_from_angle_speed(math.pi/3, 5), 2.5)
assert_equal(x_from_angle_speed(math.pi/2, 5), 0.0)
assert_equal(x_from_angle_speed(2*math.pi/3, 5), -2.5)
assert_equal(x_from_angle_speed(math.pi, 5), -5.0)
assert_equal(x_from_angle_speed(-math.pi/3, 5), 2.5)
assert_equal(x_from_angle_speed(-math.pi/2, 5), 0.0)
assert_equal(x_from_angle_speed(-2*math.pi/3, 5), -2.5)

################################################################################
## Testing y_from_angle_speed
assert_equal(y_from_angle_speed(0, 5), 0.0)
assert_equal(y_from_angle_speed(math.pi/6, 5), 2.5)
assert_equal(y_from_angle_speed(math.pi/2, 5), 5.0)
assert_equal(y_from_angle_speed(5*math.pi/6, 5), 2.5)
assert_equal(y_from_angle_speed(math.pi, 5), 0.0)
assert_equal(y_from_angle_speed(-math.pi/6, 5), -2.5)
assert_equal(y_from_angle_speed(-math.pi/2, 5), -5.0)
assert_equal(y_from_angle_speed(-5*math.pi/6, 5), -2.5)

################################################################################
## Testing is_dot_hitting_position
FIRST_POSITION = {'x': 50, 'y': 50}
SECOND_POSITION = {'x': 60, 'y': 60}
THIRD_POSITION = {'x': 70, 'y': 70}
assert_equal(is_dot_hitting_position(FIRST_POSITION, FIRST_POSITION), True)
assert_equal(is_dot_hitting_position(FIRST_POSITION, SECOND_POSITION), True)
assert_equal(is_dot_hitting_position(FIRST_POSITION, THIRD_POSITION), False)
assert_equal(is_dot_hitting_position(SECOND_POSITION, THIRD_POSITION), True)

################################################################################
## Testing check_dot_goal_reached
ORIGIN = {'x': 0, 'y': 0}
CENTER = {'x': WINDOW_WIDTH/2, 'y': WINDOW_HEIGHT/2}
CENTER_RIGHT = {'x': WINDOW_WIDTH, 'y': WINDOW_HEIGHT/2}
DOT_IN_PROGRESS = {'current': ORIGIN, 'goal': CENTER_RIGHT}
check_dot_goal_reached(DOT_IN_PROGRESS)
assert_equal(DOT_IN_PROGRESS['current'] != DOT_IN_PROGRESS['goal'], True)
assert_equal(DOT_IN_PROGRESS['goal'], CENTER_RIGHT)
DOT_FINISHED = {'current': CENTER, 'goal': CENTER}
check_dot_goal_reached(DOT_FINISHED)
assert_equal(DOT_IN_PROGRESS['current'] != DOT_IN_PROGRESS['goal'], True)
assert_equal(CENTER != DOT_IN_PROGRESS['goal'], True)

################################################################################
## Testing move_dot
ORIGIN = {'x': 0, 'y': 0}
CENTER = {'x': WINDOW_WIDTH/2, 'y': WINDOW_HEIGHT/2}
CENTER_RIGHT = {'x': WINDOW_WIDTH, 'y': WINDOW_HEIGHT/2}
GOAL_POSITION = {'x': 3, 'y': 4}
DOT_IN_PROGRESS = {'current': ORIGIN, 'goal': GOAL_POSITION}
move_dot(DOT_IN_PROGRESS)
assert_equal(DOT_IN_PROGRESS['current']['x'], .6)
assert_equal(DOT_IN_PROGRESS['current']['y'], .8)
move_dot(DOT_IN_PROGRESS)
assert_equal(DOT_IN_PROGRESS['current']['x'], 1.2)
assert_equal(DOT_IN_PROGRESS['current']['y'], 1.6)
move_dot(DOT_IN_PROGRESS)
assert_equal(DOT_IN_PROGRESS['current']['x'], 1.8)
assert_equal(DOT_IN_PROGRESS['current']['y'], 2.4)
move_dot(DOT_IN_PROGRESS)
assert_equal(DOT_IN_PROGRESS['current']['x'], 2.4)
assert_equal(DOT_IN_PROGRESS['current']['y'], 3.2)
move_dot(DOT_IN_PROGRESS)
assert_equal(DOT_IN_PROGRESS['current']['x'], 3.0)
assert_equal(DOT_IN_PROGRESS['current']['y'], 4.0)

################################################################################
## Testing update_world
ORIGIN = {'x': 0, 'y': 0}
ONE_STEP = {'x': .89442, 'y': .44721359}
CENTER = {'x': WINDOW_WIDTH/2, 'y': WINDOW_HEIGHT/2}
CENTER_RIGHT = {'x': WINDOW_WIDTH, 'y': WINDOW_HEIGHT/2}
ONE_DOT_WORLD = {'red dots': [{'current': ORIGIN, 'goal': CENTER_RIGHT}], 'score': 0}
update_world(ONE_DOT_WORLD)
assert_equal(ONE_DOT_WORLD['red dots'], [{'current': ONE_STEP, 'goal': CENTER_RIGHT}])
ONE_DOT_WORLD['red dots'][0]['current'] = ONE_DOT_WORLD['red dots'][0]['goal']
update_world(ONE_DOT_WORLD)
assert_equal(ONE_DOT_WORLD['red dots'][0]['current'] != ONE_DOT_WORLD['red dots'][0]['goal'], True)

# Note: Could probably improve these by adding worlds with more than one dot...

################################################################################
## Testing handle_motion
ORIGIN = {'x': 0, 'y': 0}
CENTER = {'x': WINDOW_WIDTH/2, 'y': WINDOW_HEIGHT/2}
CENTER_RIGHT = {'x': WINDOW_WIDTH, 'y': WINDOW_HEIGHT/2}
ONE_DOT_WORLD = {'red dots': [{'current': ORIGIN, 'goal': CENTER_RIGHT}], 'score': 0}
# Miss the dot
handle_motion(ONE_DOT_WORLD, 500, 500)
assert_equal(len(ONE_DOT_WORLD['red dots']), 1)
# Hit the dot
handle_motion(ONE_DOT_WORLD, 0, 0)
assert_equal(len(ONE_DOT_WORLD['red dots']), 2)