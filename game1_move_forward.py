'''
A picture moves forward until it hits a wall.

Demonstrates
 - Simple movement
 - Boolean flag to control action

Change log:
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.1'

import arcade, math, random
from cisc108_game import Cisc108Game

# Game Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Moving Forward!"

MOVE_SPEED = 4

# Load images
DOG_IMAGE = arcade.load_texture("doggo.png")

# Define your general world
World = {
    'x': int,
    'y': int,
    'moving?': bool
}

# Define the initial world
INITIAL_WORLD = {
    'x': WINDOW_WIDTH/4,
    'y': WINDOW_HEIGHT/2,
    'moving?': True
}

def draw_world(world: World):
    """
    Draw the world
    
    Args:
        world (World): The current state of the world.
    """
    arcade.draw_texture_rectangle(world['x'], world['y'],
                                  DOG_IMAGE.width, DOG_IMAGE.height,
                                  DOG_IMAGE)

def update_world(world: World):
    """
    Update the world (specifically, its timer and angle).
    
    Args:
        world (World): The current state of the world.
    """
    if WINDOW_WIDTH <= (world['x'] + DOG_IMAGE.width/2):
        world['moving?'] = False
        
    if world['moving?']:
        world['x'] = world['x'] + MOVE_SPEED

def handle_key(world: World, key: int):
    """
    Process keyboard input
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """

def handle_mouse(world: World, x: int, y: int, button: str):
    """
    Process mouse clicks
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked ('left', 'right', 'middle')
    """
    
def handle_motion(world: World, x: int, y: int):
    """
    Handle mouse motion.
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """


############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == "__main__":
    Cisc108Game(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse, handle_motion)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()

