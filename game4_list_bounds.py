'''
Educational game for learning about list indexes.
Given the displayed index, click the correct position in the list.

Demonstrates
 - Drawing text
 - Drawing multiple things
 - Drawing boxes
 - Using position when handling mouse press
 - Using position when handling mouse motion
 - Using a random value

Change log:
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.1'

import arcade, math, random
from cisc108_game import Cisc108Game

################################################################################
## Game Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.GOLD
GAME_TITLE = "Index the List!"

# Convenience constants based on window size
WINDOW_CENTER_X = int(WINDOW_WIDTH/2)
WINDOW_CENTER_Y = int(WINDOW_HEIGHT/2)

# These control the generated lists' length
LIST_MINIMUM_LENGTH =  3
LIST_MAXIMUM_LENGTH =  8
# These control the possible values of the generated list
LIST_MINIMUM_VALUE  = -9
LIST_MAXIMUM_VALUE  =  9

# The size of the list's boxes
FONT_SIZE = 20
BOX_WIDTH = 40
BOX_HEIGHT = 80

################################################################################
## Helper Functions

def random_value() -> int:
    '''
    Return a random number for the list.
    '''
    return random.randint(LIST_MINIMUM_VALUE, LIST_MAXIMUM_VALUE)

def random_list() -> [int]:
    '''
    Return a randomly-sized list of random values.
    '''
    values = []
    random_length = random.randint(LIST_MINIMUM_LENGTH, LIST_MAXIMUM_LENGTH)
    for i in range(random_length):
        values.append(random_value())
    return values

def to_screen_x(index: int, list_size: int) -> int:
    """
    Given an index in the list, and the number of elements in the
    list, compute the X coordinate of the box on the screen.
    
    Args:
        index (int): The index within the list.
        list_size (int): The number of elements in the list.
    Returns:
        int: The horizontal position of the index on the screen.
    """
    boxes_left_x = WINDOW_CENTER_X - (list_size/2 * BOX_WIDTH)
    index_offset = index * BOX_WIDTH
    return int(boxes_left_x + index_offset)

def to_box_index(x: int, list_size: int) -> int:
    """
    Given an x coordinate on the screen, and the number of elements in the
    list, compute the index that this position refers to in the list.
    The X position is expected to be within the boxes drawn on the screen,
    or result will be meaningless.
    Effectively, this is the inverse of to_screen_x, converting the drawn
    position to the boxes index.
    
    Args:
        x (int): The x position on the screen
        list_size (int): The number of elements in the list.
    Returns:
        int: The index in the list.
    """
    boxes_left_index = list_size/2 - (WINDOW_CENTER_X/BOX_WIDTH)
    x_offset = x / BOX_WIDTH
    return int(x_offset+boxes_left_index)

def get_absolute_index(index: int, list_size: int) -> int:
    '''
    Consumes an index in a list and the maximum number of elements,
    and produces an integer representing the absolute index of the list.
    If the index was positive there is no change, but if it was negative
    then it is converted to its positive counterpart.
    
    Args:
        index (int): An index of a list.
        list_size (int): The number of values in the list.
    Returns:
        int: The absolute version of the index.
    '''
    if index < 0:
        return list_size + index
    else:
        return index

################################################################################
# World definitions

## Define the general world
World = {
    # The current list we are displaying to the player.
    'values': [int],
    # The index that the player should click
    'target': int,
    # The index that the player is hovering over
    'hovering': int,
    # The player's current score.
    'score': int
}


## Define the initial world
INITIAL_WORLD = {
    'values': random_list(),
    'target': 0,
    'score': 0,
    'hovering': None
}

################################################################################
# Drawing functions

def draw_box(filled: bool, value: int, x: int, y: int, size: int):
    '''
    Draw the box at the position with the given size.
    Potentially also fill the box.
    
    Args:
        filled (bool): Whether or not to fill the box.
        value (int): The value that should be shown inside this box.
        x (int): The x-coordinate to draw at.
        y (int): The y-coordinate to draw at.
        size (int): The height and width of the box.
    '''
    if filled:
        arcade.draw_xywh_rectangle_filled(x, y, size/2, size, arcade.color.DARK_BLUE)
    arcade.draw_xywh_rectangle_outline(x, y, size, size, arcade.color.WHITE)
    arcade.draw_text(str(value), x+5, y+5, arcade.color.WHITE, FONT_SIZE)

def draw_boxes(values: [int], hovering: int):
    '''
    Draws all the values in the given list within boxes.
    Also fills in the box at the hovering index.
    
    Args:
        values ([int]): The list of values to draw.
        hovering (int): The index of the value to fill in with color.
    '''
    index = 0
    for box_value in values:
        x = to_screen_x(index, len(values))
        y = WINDOW_CENTER_Y
        # If the current index is our hovering one, we pass in True
        draw_box(hovering==index, box_value, x, y, BOX_HEIGHT)
        index = index + 1
        
def draw_instructions(target: int):
    '''
    Draws the instructions for the game ("Click index X") at the top-left
    of the screen.
    
    Args:
        target (int): The index that the player needs to click.
    '''
    arcade.draw_text("Click index "+str(target), 0, WINDOW_HEIGHT-FONT_SIZE,
                     arcade.color.WHITE, FONT_SIZE, anchor_x='left')
    
def draw_score(score: int):
    """
    Draws the player's current score in the bottom-left corner of the
    screen.
    
    Args:
        score (int): The player's current score.
    """
    arcade.draw_text("Score: "+str(score), 0, 0, arcade.color.WHITE, FONT_SIZE)

def draw_world(world: World):
    """
    Draw the world
    
    Args:
        world (World): The current state of the world.
    """
    draw_boxes(world['values'], world['hovering'])
    draw_score(world['score'])
    draw_instructions(world['target'])

################################################################################
# World manipulating functions

def update_world(world: World):
    """
    Do nothing to update the world.
    
    Args:
        world (World): The current state of the world.
    """

def handle_key(world: World, key: int):
    """
    Ignore keyboard input
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """

def win_point(world: World):
    """
    Increase the player's score, resets the list to a new randomly sized
    list of random values, and choose a new target index randomly from the list.
    
    Args:
        world (World): The current state of the world.
    """
    world['values'] = random_list()
    maximum_index = len(world['values'])
    world['target'] = random.randint(-maximum_index, maximum_index-1)
    world['score'] += 1
    
def lose_point(world: World):
    '''
    Decreases a point from the player's score.
    
    Args:
        world (World): The current state of the world.
    '''
    world['score'] -= 1

def handle_mouse(world: World, x: int, y: int, button: int):
    """
    Process mouse clicks by determining if the player clicked
    the target index (winning a point) or not (losing a point).
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked ('left', 'right', 'middle')
    """
    clicked_index = to_box_index(x, len(world['values']))
    target_index = get_absolute_index(world['target'], len(world['values']))
    if clicked_index == target_index:
        win_point(world)
    else:
        lose_point(world)
        
def handle_motion(world: World, x: int, y: int):
    """
    Handle mouse motion to update the currently hovered-over box.
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """
    hovered_index = to_box_index(x, len(world['values']))
    if 0 <= hovered_index < len(world['values']):
        world['hovering'] = hovered_index
    else:
        world['hovering'] = None

############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == '__main__':
    Cisc108Game(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse, handle_motion)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()
