import arcade, math, random
from cisc108_game import Cisc108Game

# Game Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60

TIMER_MAXIMUM = 100

# Load images
CISC108_LOGO = arcade.load_texture("cisc108_banner.png")

# Define your general world
World = {
    'angle': int,
    'phase': str,
    'timer': int
}

# Define the initial world
INITIAL_WORLD = {
    'angle': 0,
    'phase': 'waiting',
    'timer': 0
}

# Game Functions

def draw_world(world: World):
    """
    Draw the world
    
    Args:
        world (World): The current state of the world.
    """
    arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                                  CISC108_LOGO.width, CISC108_LOGO.height,
                                  CISC108_LOGO,
                                  world['angle'])

# Map phases to their next phase
NEXT_PHASE = {
    'spinning forward': 'waiting',
    'waiting': 'spinning backward',
    'spinning backward': 'waiting again',
    'waiting again': 'spinning forward'
    }
        
def update_timer(world: World):
    """
    Increments the world's timer, until it hits the TIMER_MAXIMUM.
    Then it resets the timer and shifts to the next phase.
    
    Args:
        world (World): The current state of the world.
    """
    if world['timer'] < TIMER_MAXIMUM:
        world['timer'] += 1
    else:
        world['timer'] = 0
        world['phase'] = NEXT_PHASE[world['phase']]
        
def update_angle(world: World):
    """
    Sets the world's angle based on the current phase and the progress
    of the timer towards the TIMER_MAXIMUM.
    
    Args:
        world (World): The current state of the world.
    """
    progress = world['timer']/TIMER_MAXIMUM
    if world['phase'] == 'spinning forward':
        world['angle'] = 360 * progress
    elif world['phase'] == 'spinning backward':
        world['angle'] = 360 * (1 - progress)
    else:
        world['angle'] = 0

def update_world(world: World):
    """
    Update the world (specifically, its timer and angle).
    
    Args:
        world (World): The current state of the world.
    """
    update_timer(world)
    update_angle(world)

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

