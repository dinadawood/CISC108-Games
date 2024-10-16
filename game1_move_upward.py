'''
A picture moves upward until it hits a wall.

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
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.GOLD
GAME_TITLE = "Mario Moves Upwards!"

MOVE_SPEED = 7

# Load images
MARIO_IMAGE = arcade.load_texture("mario2.png")

# Define your general world
World = {
    'x': int,
    'y': int,
    #'moving?': bool
    #The direction represents a str that displays an image moving up or down
    'direction': str
}

# Define the initial world
INITIAL_WORLD = {
    'x': WINDOW_WIDTH/4,
    'y': WINDOW_HEIGHT/2,
    #'moving?': True
    'direction': 'up'
}

def draw_world(world: World):
    """
    Draw the world
    
    Args:
        world (World): The current state of the world.
    """
    arcade.draw_texture_rectangle(world['x'], world['y'],
                                  MARIO_IMAGE.width, MARIO_IMAGE.height,
                                  MARIO_IMAGE)

def update_world(world: World):
    """
    Update the world (specifically, its timer and angle).
    
    Args:
        world (World): The current state of the world.
    """
    
    if WINDOW_HEIGHT <= (world['y'] + MARIO_IMAGE.height/2):
        world['direction'] = 'down'
        
    if(world['y'] - MARIO_IMAGE.width/2) <= 0:
        world['direction'] = 'up'
        
    if world['direction'] == 'up':
        world['y'] = world['y'] + MOVE_SPEED
    elif world['direction'] == 'down':
        world['y'] = world['y'] - MOVE_SPEED
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
        button (str): The button that was clicked ('up', 'down')
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


