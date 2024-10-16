'''
Click the image when you see Ada, but don't click
when you see a Potato.

Demonstrates:
 - Timers to control action
 - Responding to mouse press
 - Drawing text
 - Switching images

Change log:
 - 0.0.1: Initial version
'''
__VERSION__ = '0.0.1'

import arcade, math, random
from cisc108_game import Cisc108Game

# Game Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.DARK_GREEN
GAME_TITLE = "Ada or Potato?"

SWITCH_TIMER = 60

# Define your general world
World = {
    'mode': str,
    'timer': int,
    'score': int
}

# Define the initial world
INITIAL_WORLD = {
    'mode': 'ada',
    'timer': SWITCH_TIMER,
    'score': 0
}

# Load images
ADA = arcade.load_texture('ada.png')
POTATO = arcade.load_texture('potato.png')

def draw_image_centered(image: arcade.Texture):
    """
    Draws the given image in the very center of the window.
    
    Args:
        image (Texture): The image to be drawn.
    """
    arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                                  image.width, image.height, image)

def draw_world(world: World):
    """
    Draw the world
    
    Args:
        world (World): The current state of the world.
    """
    if world['mode'] == 'ada':
        draw_image_centered(ADA)
    elif world['mode'] == 'potato':
        draw_image_centered(POTATO)
    arcade.draw_text(str(world['score']), 0, 0, arcade.color.WHITE, 50)
    
def switch_mode(world: World):
    """
    Swaps the world's image between either Ada or Potato.
    
    Args:
        world (World): The current state of the world.
    """
    if world['mode'] == 'ada':
        world['mode'] = 'potato'
    else:
        world['mode'] = 'ada'

def update_world(world: World):
    """
    Update the world's timer and image.
    
    Args:
        world (World): The current state of the world.
    """
    if world['timer'] > 0:
        world['timer'] -= 1
    else:
        world['timer'] = SWITCH_TIMER
        switch_mode(world)

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
    if world['mode'] == 'ada':
        world['score'] += 1
    else:
        world['score'] -= 1

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

