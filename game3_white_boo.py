'''
Simple game where you catch the white boo. Every time you catch a boo,
two new ones appear in their place.

Demonstrates
 - Drawing multiple things
 - Drawing boos
 - Moving things in a direction with a speed
 - Handling circular collisions
 - Using position when handling mouse press
 - Using a random value

Change log:
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.1'

import arcade, math, random
from cisc108_game import Cisc108Game

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = arcade.color.GOLD
GAME_TITLE = "Get the White Boo!"

WHITE_BOO_SIZE = 50
BOO_SPEED = 10

# Create a white boo image to represent our laser pointer
# Load images
LASER_POINTER = arcade.load_texture("white_boo.png")

################################################################################
## Record definitions

# A position is an X/Y coordinate pair.
Position = { 'x': int, 'y': int }

WhiteBoo = {
    # The WhiteBoo's current drawn position
    'current': Position,
    # Where the WhiteBoo is going towards
    'goal': Position,
    'age': int
}

################################################################################
## Helper Functions

def make_random_position() -> Position:
    '''
    Produce a new random position (random X/Y coordinate) within the
    bounds of the window.
    
    Returns:
        Position: The new random position.
    '''
    return {
        'x': random.randint(0, WINDOW_WIDTH),
        'y': random.randint(0, WINDOW_HEIGHT)
    }

def make_white_boo() -> WhiteBoo:
    '''
    Produces a new boo with a random current position and random
    goal position.
    
    Returns:
        WhiteBoo: The new randomly generated white boo.
    '''
    return {
        'current': make_random_position(),
        'goal': make_random_position(),
        'age': 0
    }

def angle_between(p1: Position, p2: Position) -> float:
    '''
    Uses trigonometry to determine the angle (in radians) between
    two points. The result ranges from pi to -pi radians (which would be
    180 degrees and negative 180 degrees).
    
    Args:
        p1 (Position): The origin position
        p2 (Position): The target position
    Returns:
        float: The angle in radians between the origin and the target.
    '''
    return math.atan2(p2['y']-p1['y'], p2['x']-p1['x'])

def distance_between(p1: Position, p2: Position) -> float:
    '''
    Uses algebra to determine the distance between two points.
    
    Args:
        p1 (Position): The origin position
        p2 (Position): The target position
    Returns:
        float: The distance in pixels between the two points.
    '''
    return math.sqrt((p2['y']-p1['y'])**2+(p2['x']-p1['x'])**2)

def x_from_angle_speed(angle: float, speed: float) -> float:
    """
    Determines the new X-coordinate when you move `speed` pixels
    in the `angle` direction. The angle is in radians.
    
    Args:
        angle (float): The angle to move in radians.
        speed (float): The number of pixels to move in that direction.
    Returns:
        float: The horizontal distance traveled
    """
    return math.cos(angle) * speed

def y_from_angle_speed(angle: float, speed: float) -> float:
    """
    Determines the new Y-coordinate when you move `speed` pixels
    in the `angle` direction. The angle is in radians.
    
    Args:
        angle (float): The angle to move in radians.
        speed (float): The number of pixels to move in that direction.
    Returns:
        float: The vertical distance traveled
    """
    return math.sin(angle) * speed

def is_boo_hitting_position(boo: Position, position: Position) -> bool:
    '''
    Determine if the boo's position is colliding with the given point.
    The boo has a size (WHITE_BOO_SIZE) that allows for some tolerance, so
    that the points don't have to be exactly on top of each other.
    
    Args:
        boo (Position): The boo's position to be checking.
        position (Position): The position to be checking.
    Returns:
        bool: Whether the boo is hitting that position
    '''
    return distance_between(boo, position) < WHITE_BOO_SIZE

################################################################################
# World definitions

World = {
    # The list of white boos currently in the world.
    'white boos': [WhiteBoo],
    # The current score for the user
    'score': int
}

# Define the initial world
INITIAL_WORLD = {
    # Start off with one white boo
    'white boos': [make_white_boo()],
    'score': 0
}

################################################################################
# Drawing functions

def draw_boo(boo: WhiteBoo):
    '''
    Draw the given white boo on screen.
    
    Args:
        boo (WhiteBoo): The white boo to draw
    '''
    angle = math.degrees(angle_between(boo['current'], boo['goal']))
    arcade.draw_texture_rectangle(boo['current']['x'], boo['current']['y'],
                                  WHITE_BOO_SIZE, WHITE_BOO_SIZE, LASER_POINTER, angle +180)
    
def draw_score(score: int):
    '''
    Draw the given score in the bottom-left corner.
    
    Args:
        score (int): The score to draw.
    '''
    arcade.draw_text(str(score), 0, 0, arcade.color.WHITE, 20)

def draw_world(world: World):
    """
    Draw all the boos and the current score.
    
    Args:
        world (World): The current world to draw
    """
    for white_boo in world['white boos']:
        draw_boo(white_boo)
    draw_score(world['score'])
    
################################################################################
# Boo manipulating functions

def check_boo_goal_reached(boo: WhiteBoo):
    '''
    Tests whether the boo has reached its goal; if so, it resets to a new
    goal position.
    
    Args:
        boo (WhiteBoo): The white boo to be testing and potentially updating.
    '''
    if is_boo_hitting_position(boo['current'], boo['goal']):
        boo['goal'] = make_random_position()
    
def move_boo(boo: WhiteBoo):
    '''
    Moves the white boo towards its goal.
    
    Args:
        boo (WhiteBoo): The white boo to be moving.
    '''
    angle = angle_between(boo['current'], boo['goal'])
    speed = BOO_SPEED + boo['age']
    boo['current']['x'] += x_from_angle_speed(angle, speed)
    boo['current']['y'] += y_from_angle_speed(angle, speed)
    boo['age'] += 1/12
    
################################################################################
# World manipulating functions

def update_world(world: World):
    """
    Updates the world by moving all the boos and checking if
    they've reached their goals.
    
    Args:
        world (World): The current world
    """
    for boo in world['white boos']:
        move_boo(boo)
        check_boo_goal_reached(boo)

def handle_key(world: World, key: int):
    """ Process keyboard input """

def handle_mouse(world: World, x: int, y: int, button: int):
    """ Process mouse clicks """
    
def handle_motion(world: World, x: int, y: int):
    """
    Handle the mouse moving by iterating through the white boos
    and retaining boos that are not touching the mouse. If a
    white boo is touched, it is filtered out and two new white boos
    are added instead.
    """
    kept_boos = []
    mouse_position = {'x': x, 'y': y}
    for boo in world['white boos']:
        if is_boo_hitting_position(boo['current'], mouse_position):
            # Make two new white boos
            kept_boos.append(make_white_boo())
            kept_boos.append(make_white_boo())
        else:
            # Leave boo unchanged
            kept_boos.append(boo)
    world['white boos'] = kept_boos[:40]

############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == '__main__':
    Cisc108Game(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse, handle_motion)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()

