'''
    Very simple game of coloring the squares.
    You have a palette of 16 colors
    and some space to create your
    own little masterpiece.

Demonstrates
 - Drawing a grid of squares
 - Drawing a palette of colors
 - Using mouse handle press to fill in
     squares with the color chosen.
 - Mouse handle press on a square with
     a color with make the block white again.

Change log:
  - 0.0.2: Added support for handle_release
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.2'

import arcade, math, random
from cisc108_game import Cisc108Game

################################################################################
## Game Constants

BACKGROUND_COLOR = arcade.color.LIGHT_BLUE
GAME_TITLE = "Coloring Squares"

# Set how many rows and columns we will have
ROW_COUNT = 16
COLUMN_COUNT = 16

# The number of squares horizontally and vertically in our grid
WIDTH = 50
HEIGHT = 30

# This sets the margin between the squares
# and the edges of the screen.
MARGIN = 5

# The number of squares horizontally and vertically in our grid including margins
WINDOW_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
WINDOW_HEIGHT = (WIDTH + MARGIN) * ROW_COUNT + MARGIN

# How big each square will be on the grid.
SQUARE_SIZE = 25

################################################################################
## Helper functions

# Make square images: Colors of the rainbow w/ some shades and mixes
PINK_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.PINK)
RED_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.RED)
DARK_RED_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.DARK_RED)
ORANGE_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.ORANGE)
YELLOW_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.YELLOW)
LIGHT_GREEN_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.LIGHT_GREEN)
GREEN_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.GREEN)
DARK_GREEN_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.DARK_GREEN)
CYAN_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.CYAN)
BLUE_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.BLUE)
DARK_BLUE_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.DARK_BLUE)
PURPLE_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.PURPLE)
BROWN_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.BROWN)
WHITE_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.WHITE)
GRAY_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.GRAY)
BLACK_SQUARE = arcade.make_soft_square_texture(SQUARE_SIZE, arcade.color.BLACK)

# We can map the string versions of colors to the texture with a dictionary
SQUARE_COLOR_TEXTURES = {
    'pink': PINK_SQUARE,
    'red': RED_SQUARE,
    'dark red': DARK_RED_SQUARE,
    'orange': ORANGE_SQUARE,
    'yellow': YELLOW_SQUARE,
    'light green': LIGHT_GREEN_SQUARE,
    'green': GREEN_SQUARE,
    'dark green': DARK_GREEN_SQUARE,
    'cyan': CYAN_SQUARE,
    'blue': BLUE_SQUARE,
    'dark blue': DARK_BLUE_SQUARE,
    'purple': PURPLE_SQUARE,
    'brown': BROWN_SQUARE,
    'white': WHITE_SQUARE,
    'gray': GRAY_SQUARE,
    'black': BLACK_SQUARE
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
            # Appending the colors to a cell/square
            if y == 0 and x == 0:
                row.append('pink')
            elif y == 0 and x == 1:
                row.append('red')
            elif y == 0 and x == 2:
                row.append('dark red')
            elif y == 0 and x == 3:
                row.append('orange')
            elif y == 0 and x == 4:
                row.append('yellow')
            elif y == 0 and x == 5:
                row.append('light green')
            elif y == 0 and x == 6:
                row.append('green')
            elif y == 0 and x == 7:
                row.append('dark green')
            elif y == 0 and x == 8:
                row.append('cyan')
            elif y == 0 and x == 9:
                row.append('blue')
            elif y == 0 and x == 10:
                row.append('dark blue')
            elif y == 0 and x == 11:
                row.append('purple')
            elif y == 0 and x == 12:
                row.append('brown')
            elif y == 0 and x == 13:
                row.append('white')
            elif y == 0 and x == 14:
                row.append('gray')
            elif y == 0 and x == 15:
                row.append('black')
            else:
                row.append(color)
        # Add this row to the grid
        grid.append(row)
    return grid

################################################################################
## Record definitions

World = {
    # A list of lists of strings representing a 2D grid of colors
    'grid': [[str]],
    # These keep track of the latest mouse position within the grid.
    'x': int,
    'y': int,
    'color': str
}

INITIAL_WORLD = {
    'grid': make_grid_color(WINDOW_WIDTH, WINDOW_HEIGHT, 'white'),
    'x': None,
    'y': None,
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
    the string colors into the actual colored square images.
    
    Args:
        grid ([[str]]): The list of lists (a 2-Dimensional list) of colors.
    '''
    # We need to know the x and y to draw at.
    # We'll use the counting pattern to calculate the x and y.
    y = 0
    for row in grid:
        x = 0
        for cell_color in row:
            square_image = SQUARE_COLOR_TEXTURES[cell_color]
            arcade.draw_xywh_rectangle_textured(x*SQUARE_SIZE, y*SQUARE_SIZE,
                                                SQUARE_SIZE, SQUARE_SIZE,
                                                square_image)
            x += 1
        y += 1
#        #Figure out where the box is
#        x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
#        y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
#
#        # Draw the box
#        arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

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
    grid_x = world['x']
    grid_y = world['y']
    # Is the mouse on a grid cell?
    if grid_x != None and grid_y != None:
        advance_grid_cell_color(world['grid'], grid_x, grid_y)
        
def advance_grid_cell_color(grid: [[str]], grid_x: int, grid_y: int):
    # Look up the old color (note that it's row/column, so y comes first)
    if (grid_y == 0 and grid_x == 0) or (grid_y == 0 and grid_x == 1) or (grid_y == 0 and grid_x == 2) or (grid_y == 0 and grid_x == 3) or (grid_y == 0 and grid_x == 4) or (grid_y == 0 and grid_x == 5) or (grid_y == 0 and grid_x == 6) or (grid_y == 0 and grid_x == 7) or (grid_y == 0 and grid_x == 8) or (grid_y == 0 and grid_x == 9) or (grid_y == 0 and grid_x == 10) or (grid_y == 0 and grid_x == 11) or (grid_y == 0 and grid_x == 12) or (grid_y == 0 and grid_x == 13) or (grid_y == 0 and grid_x == 14) or (grid_y == 0 and grid_x == 15):
        old_color = grid[grid_y][grid_x]
        grid[grid_y][grid_x] = old_color
    else:
        old_color = grid[grid_y][grid_x]
        # Advance that color in the sequence
        new_color = advance_color(old_color)
        # Mutate the grid by updating the list of list's value with the new color.
        #   This is weird! We usually hate updating a value in a list this way,
        #   but sometimes it is convenient.
        grid[grid_y][grid_x] = new_color
        
def handle_key(world: World, key: int):
    """
    Nothing happens when we press the key.
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """
    if key == ord('r'):
       world['grid'] = make_grid_color(WINDOW_WIDTH, WINDOW_HEIGHT, 'white')
            

def handle_mouse(world: World, x: int, y: int, button: str):
    """
    Nothing happens you press the mouse button.
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked ('left', 'right', 'middle')
    """
    column = int(x // (WINDOW_WIDTH + MARGIN))
    row = int(y // (WINDOW_HEIGHT + MARGIN))

    print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

    # Make sure we are on-grid. It is possible to click in the upper right
    # corner in the margin and go to a grid location that doesn't exist
    if row < ROW_COUNT and column < COLUMN_COUNT:

    # Flip the location between 1 and 0.
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

def handle_motion(world: World, x: int, y: int):
    """
    Clicking a square applies color that's chosen from palette.
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """
    # First we translate from the position within the window to the
    #   position within the grid of squares
    grid_x = screen_to_grid(x, WINDOW_WIDTH, WIDTH)
    grid_y = screen_to_grid(y, WINDOW_HEIGHT, HEIGHT)
    # If we're out of bounds, then we set the values to None
    if grid_x < 0 or grid_x >= WINDOW_WIDTH:
        grid_x = None
    if grid_y < 0 or grid_y >= WINDOW_HEIGHT:
        grid_y = None
    # Then we update our world to keep track of the latest mouse
    #   movements within the grid.
    world['x'] = grid_x
    world['y'] = grid_y
    
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
        width (int): The number of values in the target coordinate system.
    Returns:
        int: The scaled value in the other coordinate system.
    '''
    return int(coordinate * grid_size / screen_size)

def advance_color(old_color: str) -> str:
    '''
    Consumes a color (string) and produces the next color in the
    sequence 
    
    Args:
        old_color (str): The current color string
    Returns:
        str: The next color in the sequence...
    '''
    if old_color == 'pink':
        new_color = 'red'
    elif old_color == 'red':
        new_color = 'dark red'
    elif old_color == 'dark red':
        new_color = 'orange'
    elif old_color == 'orange':
        new_color = 'yellow'
    elif old_color == 'yellow':
        new_color = 'light green'
    elif old_color == 'light green':
        new_color = 'green'
    elif old_color == 'green':
        new_color = 'dark green'
    elif old_color == 'dark green':
        new_color = 'cyan'
    elif old_color == 'cyan':
        new_color = 'blue'
    elif old_color == 'blue':
        new_color = 'dark blue'
    elif old_color == 'dark blue':
        new_color = 'purple'
    elif old_color == 'purple':
        new_color = 'brown'
    elif old_color == 'brown':
        new_color = 'white'
    elif old_color == 'white':
        new_color = 'gray'
    elif old_color == 'gray':
        new_color = 'black'
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
