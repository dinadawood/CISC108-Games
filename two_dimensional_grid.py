'''
Hover your mouse over the circles in a grid to make them flash colors.
A simple example of a mutable 2-D grid. This would be useful
for several of the projects!

Warning: this game has flashing circles!

Change log:
  - 0.0.1: Initial version (using 0.0.4 of cisc108_game.py)
'''
__VERSION__ = '0.0.1'

import arcade, math, random
from cisc108_game import Cisc108Game

################################################################################
## Game Constants

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Fun on a 2D grid"

# The number of circles horizontally and vertically in our grid
GRID_WIDTH = 25
GRID_HEIGHT = 25
# How big a circle will be.
CIRCLE_SIZE = 20

# Make three circle images: red, blue, and green.
RED_CIRCLE = arcade.make_circle_texture(CIRCLE_SIZE, arcade.color.RED)
BLUE_CIRCLE = arcade.make_circle_texture(CIRCLE_SIZE, arcade.color.BLUE)
GREEN_CIRCLE = arcade.make_circle_texture(CIRCLE_SIZE, arcade.color.GREEN)

# We can map the string versions of colors to the texture with a dictionary
CIRCLE_COLOR_TEXTURES = {
    'red': RED_CIRCLE,
    'blue': BLUE_CIRCLE,
    'green': GREEN_CIRCLE
}

################################################################################
## Helper functions

def make_grid_color(width: int, height: int, color: str) -> [[str]]:
    '''
    Make a 2D list (list of lists) of the given width and height,
    where every cell has the given color.
    
    Args:
        width (int): The number of elements in each row.
        height (int): The number of rows.
        color (str): The color string to put in each cell.
    '''
    grid = []
    # y will be 0..height
    for y in range(height):
        row = []
        # x will be 0..width
        for x in range(width):
            # Add this cell to the row
            row.append(color)
        # Add this row to the grid
        grid.append(row)
    return grid

################################################################################
## Record definitions

World = {
    # A list of lists of strings representing a 2D grid of colors (either
    #  'red', 'blue', or 'green').
    'grid': [[str]],
    # These keep track of the latest mouse position within the grid.
    'current mouse x': int,
    'current mouse y': int
}

INITIAL_WORLD = {
    'grid': make_grid_color(GRID_WIDTH, GRID_HEIGHT, 'red'),
    'current mouse x': None,
    'current mouse y': None
}


################################################################################
# Drawing functions

def draw_world(world: World):
    """
    Draws the current grid.
    
    Args:
        world (World): The current world to draw
    """
    draw_grid(world['grid'])
    
def draw_grid(grid: [[str]]):
    '''
    Draw the 2D list of colors horizontally and vertically, turning
    the string colors into the actual colored circle images.
    
    Args:
        grid ([[str]]): The list of lists (a 2-Dimensional list) of colors.
    '''
    # We need to know the x and y to draw at.
    # We could have also used the built-in enumerate function to get
    # the x/y indexes of each cell.
    # But instead, we'll use the counting pattern to calculate the x and y.
    y = 0
    for row in grid:
        x = 0
        for cell_color in row:
            circle_image = CIRCLE_COLOR_TEXTURES[cell_color]
            arcade.draw_xywh_rectangle_textured(x*CIRCLE_SIZE, y*CIRCLE_SIZE,
                                                CIRCLE_SIZE, CIRCLE_SIZE,
                                                circle_image)
            x += 1
        y += 1

################################################################################
# World manipulating functions

def update_world(world: World):
    """
    Every step, we update the grid cell's color at wherever
    the mouse currently is.
    
    Args:
        world (World): The current world to update.
    """
    # We get the current mouse position
    grid_x = world['current mouse x']
    grid_y = world['current mouse y']
    # Is the mouse on a grid cell?
    if grid_x != None and grid_y != None:
        advance_grid_cell_color(world['grid'], grid_x, grid_y)

def advance_grid_cell_color(grid: [[str]], grid_x: int, grid_y: int):
    # Look up the old color (note that it's row/column, so y comes first)
    old_color = grid[grid_y][grid_x]
    # Advance that color in the sequence
    new_color = advance_color(old_color)
    # Mutate the grid by updating the list of list's value with the new color.
    #   This is weird! We usually hate updating a value in a list this way,
    #   but sometimes it is convenient.
    grid[grid_y][grid_x] = new_color
    '''
    # Alternativey, we could have done a more complex bit of list processing.
    #   but then we'd have to return a new grid instead of modifying the given
    #   grid. This requires a lot of work to update a single square, but is
    #   immutable. There's always tradeoffs!
    new_grid = []
    y = 0
    for row in grid:
        x = 0
        for old_color in row:
            if x == grid_x and y == grid_y:
                new_grid.append(new_color)
            else:
                new_grid.append(old_color)
            x += 1
        y += 1
    return grid
    '''
        
def handle_key(world: World, key: int):
    """
    Nothing happens when we press the key.
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """

def handle_mouse(world: World, x: int, y: int, button: str):
    """
    Nothing happens you press the mouse button.
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked ('left', 'right', 'middle')
    """

def handle_motion(world: World, x: int, y: int):
    """
    Moving over a circle changes it to a new color.
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """
    # First we translate from the position within the window to the
    #   position within the grid of circles
    grid_x = screen_to_grid(x, WINDOW_WIDTH, GRID_WIDTH)
    grid_y = screen_to_grid(y, WINDOW_HEIGHT, GRID_HEIGHT)
    # If we're out of bounds, then we set the values to None
    if grid_x < 0 or grid_x >= GRID_WIDTH:
        grid_x = None
    if grid_y < 0 or grid_y >= GRID_HEIGHT:
        grid_y = None
    # Then we update our world to keep track of the latest mouse
    #   movements within the grid.
    world['current mouse x'] = grid_x
    world['current mouse y'] = grid_y
    
def screen_to_grid(coordinate: float, screen_size: int, grid_size: int) -> int:
    '''
    Converts a coordinate (either the x part or the y part) from a position
    within the window to the equivalent position within the grid. It does this by
    scaling the between the two different sizes.
    
    Think about this as a number line. If you have the coordinate 50 on that
    number line, and the number line's maximum value was 100 (screen_size),
    then scaling that a number line with the maximum value of 20 (grid_size) would
    give you the new coordinate 10.
    
    Args:
        coordinate (float): Either an X or Y value in a coordinate system.
        screen_size (int): The number of values in the original coordinate system.
        grid_width (int): The number of values in the target coordinate system.
    Returns:
        int: The scaled value in the other coordinate system.
    '''
    return int(coordinate * grid_size / screen_size)

def advance_color(old_color: str) -> str:
    '''
    Consumes a color (string) and produces the next color in the
    sequence red->blue->green. Only accepts those three colors.
    
    Args:
        old_color (str): The current color string (either 'red', 'blue', or 'green').
    Returns:
        str: The next color in the sequence (either 'red', 'blue', or 'green').
    '''
    if old_color == 'red':
        new_color = 'blue'
    elif old_color == 'blue':
        new_color = 'green'
    elif old_color == 'green':
        new_color = 'red'
    return new_color
    
def handle_release(world: World, key: int):
    """
    Nothing happens when you release a keyboard key.
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the released keyboard key (use ord and chr).
    """

############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == '__main__':
    Cisc108Game(World, WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse,
                handle_motion, handle_release)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()

