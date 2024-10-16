from cisc108 import assert_equal
from game4_list_bounds import *

__VERSION__ = '0.0.1'

# Need to be able to quickly make test worlds.
def make_test_world() -> World:
    return {
        'values': random_list(),
        'target': 0,
        'score': 0,
        'hovering': None
    }

################################################################################
## Testing random_value
# Testing random functions is hard! Three strategies: assert that it produces
# values within a range, generate many tests programmatically, and unit test
# based on a seed to make it deterministic (predictable). But we don't expect
# much from tests on random functions. Isolate the randomness to a helper
# function, and focus on testing the rest of the behavior.

random.seed(0)

# Test the function produces values in the expected range
for i in range(4):
    assert_equal(LIST_MINIMUM_VALUE <= random_value() <= LIST_MAXIMUM_VALUE, True)

################################################################################
## Testing random_list
for i in range(4):
    a_list = random_list()
    # Ensure that the list is within the expected range length.
    assert_equal(LIST_MINIMUM_LENGTH <= len(a_list) <= LIST_MAXIMUM_LENGTH, True)
    # We don't want all values to be the same, which is unlikely if we're
    # generating random numbers.
    assert_equal(a_list[0] != a_list[1] and a_list[1] != a_list[2], True)

################################################################################
## Testing to_screen_x
    
# Test small list over various indices
assert_equal(to_screen_x(0, 5), WINDOW_CENTER_X - 125)
assert_equal(to_screen_x(1, 5), WINDOW_CENTER_X - 125 + 50)
assert_equal(to_screen_x(4, 5), WINDOW_CENTER_X - 125 + 200)

# Test bigger list over various indices
assert_equal(to_screen_x(0, 8), WINDOW_CENTER_X - 200)
assert_equal(to_screen_x(1, 8), WINDOW_CENTER_X - 200 + 50)
assert_equal(to_screen_x(4, 8), WINDOW_CENTER_X - 200 + 200)

################################################################################
## Testing to_box_index

# Test cursor exactly on start of boxes
assert_equal(to_box_index(WINDOW_CENTER_X-125, 5), 0)
assert_equal(to_box_index(WINDOW_CENTER_X-125+50, 5), 0)
assert_equal(to_box_index(WINDOW_CENTER_X-125+200, 5), 4)
# Try cursor slightly to the right of the boxes
assert_equal(to_box_index(WINDOW_CENTER_X-125+1, 5), 0)
assert_equal(to_box_index(WINDOW_CENTER_X-125+50+1, 5), 0)
assert_equal(to_box_index(WINDOW_CENTER_X-125+200+1, 5), 4)
# Try cursor slightly to the left of the boxes
assert_equal(to_box_index(WINDOW_CENTER_X-125+50-1, 5), 0)
assert_equal(to_box_index(WINDOW_CENTER_X-125+200-1, 5), 4)
# Try a few bigger boxes
assert_equal(to_box_index(WINDOW_CENTER_X - 200, 8), -1)
assert_equal(to_box_index(WINDOW_CENTER_X - 200 + 50, 8), 0)
assert_equal(to_box_index(WINDOW_CENTER_X - 200 + 200, 8), 4)

################################################################################
## Testing get_absolute_index

# Test positive indexes
assert_equal(get_absolute_index(0, 5), 0)
assert_equal(get_absolute_index(3, 5), 3)
assert_equal(get_absolute_index(4, 5), 4)
assert_equal(get_absolute_index(4, 8), 4)
# Test negative indexes
assert_equal(get_absolute_index(-1, 5), 4)
assert_equal(get_absolute_index(-3, 5), 2)
assert_equal(get_absolute_index(-4, 5), 1)
assert_equal(get_absolute_index(-5, 5), 0)
assert_equal(get_absolute_index(-4, 8), 4)

################################################################################
## Testing win_point

for i in range(4):
    TEST_WORLD = make_test_world()

    # Confirm that the world's values change
    old_values = TEST_WORLD['values']
    win_point(TEST_WORLD)
    assert_equal(old_values != TEST_WORLD['values'], True)

    # Target should be a valid index in the list
    assert_equal(-len(TEST_WORLD['values']) <= TEST_WORLD['target'] <= len(TEST_WORLD['values'])-1, True)

    # Score should be increased
    assert_equal(TEST_WORLD['score'], 1)

################################################################################
## Testing lose_point
TEST_WORLD = make_test_world()
lose_point(TEST_WORLD)
assert_equal(TEST_WORLD['score'], -1)
lose_point(TEST_WORLD)
assert_equal(TEST_WORLD['score'], -2)

################################################################################
## Testing handle_mouse
TEST_WORLD = make_test_world()

# Completely missed
TEST_WORLD['values'] = [1, 2, 3, 4]
TEST_WORLD['target'] = 0
handle_mouse(TEST_WORLD, 0, 0, 'left')
assert_equal(TEST_WORLD['score'], -1)
# Hit first index (correct)
TEST_WORLD['values'] = [1, 2, 3, 4]
TEST_WORLD['target'] = 0
handle_mouse(TEST_WORLD, 250-100, 0, 'left')
assert_equal(TEST_WORLD['score'], 0)
# Hit third index (incorrect)
TEST_WORLD['values'] = [1, 2, 3, 4]
TEST_WORLD['target'] = 0
handle_mouse(TEST_WORLD, 250-100+150, 0, 'left')
assert_equal(TEST_WORLD['score'], -1)

################################################################################
## Testing handle_motion
TEST_WORLD = make_test_world()

# Completely missed
TEST_WORLD['values'] = [1, 2, 3, 4]
handle_motion(TEST_WORLD, 0, 0)
assert_equal(TEST_WORLD['hovering'], None)
# Hit first index
TEST_WORLD['values'] = [1, 2, 3, 4]
handle_motion(TEST_WORLD, 250-100, 0)
assert_equal(TEST_WORLD['hovering'], 0)
# Hit third index
TEST_WORLD['values'] = [1, 2, 3, 4]
handle_motion(TEST_WORLD, 250-100+149, 0)
assert_equal(TEST_WORLD['hovering'], 3)
# Hit fourth index
TEST_WORLD['values'] = [1, 2, 3, 4]
handle_motion(TEST_WORLD, 250-100+150, 0)
assert_equal(TEST_WORLD['hovering'], 3)
