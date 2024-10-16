'''
Move between menus using the keyboard.

Demonstrates
  - Handling keyboard presses
  - Basic menu system

Change log:
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.1'

import arcade, math, random
from cisc108_game import Cisc108Game

# Game Constants
WINDOW_WIDTH = 725
WINDOW_HEIGHT = 575
BACKGROUND_COLOR = arcade.color.GOLD
GAME_TITLE = "Navigate the menus!"

################################################################################
## Record definitions

CAMPUS_IMAGE = arcade.load_texture('campus.png')
SMITH_IMAGE = arcade.load_texture('smith.png')
TRABANT_IMAGE = arcade.load_texture('trabant.png')
EAST_CAMPUS_IMAGE = arcade.load_texture('east_campus.png')
SECRET_IMAGE = arcade.load_texture('secret.png')
PERKINS_IMAGE = arcade.load_texture('perkins.png')

Menu = {'name': str, 'text': str, 'picture': str}

START_MENU = {'name': "University of Delaware Tour", 'text': "Let's explore campus.\nPress 'n' to advance.",
              'picture': CAMPUS_IMAGE}
FIRST_MENU = {'name': "Smith Hall", 'text': "Good place to find Dr. Bart.\nNow press 'n' again!",
              'picture': SMITH_IMAGE}
SECOND_MENU = {'name': "Trabant Hall", 'text': "You could get lunch here.\nPress 'n' to go forward.\nOr you can press 'p' to go back.",
              'picture': TRABANT_IMAGE}
THIRD_MENU = {'name': "East Campus", 'text': "Lovely looking area.\nPress 'n' to go forward.\nOr you can press 'p' to go back.",
              'picture': EAST_CAMPUS_IMAGE}
FOURTH_MENU = {'name': "Perkins", 'text': "The Hen Zone for games.\nPress 'n' to go forward.\nOr you can press 'p' to go back.",
              'picture': PERKINS_IMAGE}
LAST_MENU = {'name': "The End", 'text': "You found Ada's secret napping spot!\nCongratulations!",
              'picture': SECRET_IMAGE}

World = {'current menu': Menu}

INITIAL_WORLD = { 'current menu': START_MENU }

################################################################################
# Drawing functions

def draw_world(world: World):
    """
    Draw all the dots and the current score.
    
    Args:
        world (World): The current world to draw
    """
    picture = world['current menu']['picture']
    arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                                  picture.width, picture.height, picture)
    arcade.draw_text(world['current menu']['text'], 0, 0, arcade.color.BLACK, 20)
    arcade.draw_text(world['current menu']['name'], 0, WINDOW_HEIGHT-50,
                     arcade.color.WHITE, 50)

################################################################################
# World manipulating functions

def update_world(world: World):
    """
    Keeps the world the same.
    
    Args:
        world (World): The current world to update.
    """

def next_menu(world: World):
    if world['current menu'] == FIRST_MENU:
        world['current menu'] = SECOND_MENU
    elif world['current menu'] == SECOND_MENU:
        world['current menu'] = THIRD_MENU
    elif world['current menu'] == THIRD_MENU:
        world['current menu'] = FOURTH_MENU
    elif world['current menu'] == FOURTH_MENU:
        world['current menu'] = LAST_MENU
    elif world['current menu'] == START_MENU:
        world['current menu'] = FIRST_MENU
        
def previous_menu(world: World):
    if world['current menu'] == SECOND_MENU:
        world['current menu'] = FIRST_MENU
    elif world['current menu'] == THIRD_MENU:
        world['current menu'] = SECOND_MENU
    elif world['current menu'] == FOURTH_MENU:
        world['current menu'] = THIRD_MENU
    elif world['current menu'] == LAST_MENU:
        world['current menu'] = FOURTH_MENU
    else:
        world['current menu'] = START_MENU

def handle_key(world: World, key: int):
    """
    Process keyboard input
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """
    if key == ord('r'):
        world['current menu'] = START_MENU
    elif key == ord('n'):
        next_menu(world)
    elif key == ord('p'):
        previous_menu(world)
    elif key == ord(' '):
        world['current menu'] = LAST_MENU

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

if __name__ == '__main__':
    Cisc108Game(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse, handle_motion)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()
