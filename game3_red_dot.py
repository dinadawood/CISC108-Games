'''
Simple game where you catch the red dot. Every time you catch a dot,
two new ones appear in their place.

Demonstrates
 - Drawing multiple things
 - Drawing circles
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
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Get the Red Dot!"

RED_DOT_SIZE = 20
DOT_SPEED = 1

# Create a red circle image to represent our laser pointer
LASER_POINTER = arcade.make_circle_texture(RED_DOT_SIZE, arcade.color.RED)

################################################################################
## Record definitions

# A position is an X/Y coordinate pair.
Position = { 'x': int, 'y': int }

RedDot = {
    # The RedDot's current drawn position
    'current': Position,
    # Where the RedDot is going towards
    'goal': Position
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

def make_red_dot() -> RedDot:
    '''
    Produces a new dot with a random current position and random
    goal position.
    
    Returns:
        RedDot: The new randomly generated red dot.
    '''
    return {
        'current': make_random_position(),
        'goal': make_random_position()
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

def is_dot_hitting_position(dot: Position, position: Position) -> bool:
    '''
    Determine if the dot's position is colliding with the given point.
    The dot has a size (RED_DOT_SIZE) that allows for some tolerance, so
    that the points don't have to be exactly on top of each other.
    
    Args:
        dot (Position): The dot's position to be checking.
        position (Position): The position to be checking.
    Returns:
        bool: Whether the dot is hitting that position
    '''
    return distance_between(dot, position) < RED_DOT_SIZE

################################################################################
# World definitions

World = {
    # The list of red dots currently in the world.
    'red dots': [RedDot],
    # The current score for the user
    'score': int
}

# Define the initial world
INITIAL_WORLD = {
    # Start off with one red dot
    'red dots': [make_red_dot()],
    'score': 0
}

################################################################################
# Drawing functions

def draw_dot(dot: RedDot):
    '''
    Draw the given red dot on screen.
    
    Args:
        dot (RedDot): The red dot to draw
    '''
    arcade.draw_texture_rectangle(dot['current']['x'], dot['current']['y'],
                                  RED_DOT_SIZE, RED_DOT_SIZE, LASER_POINTER)
    
def draw_score(score: int):
    '''
    Draw the given score in the bottom-left corner.
    
    Args:
        score (int): The score to draw.
    '''
    arcade.draw_text(str(score), 0, 0, arcade.color.WHITE, 20)

def draw_world(world: World):
    """
    Draw all the dots and the current score.
    
    Args:
        world (World): The current world to draw
    """
    for red_dot in world['red dots']:
        draw_dot(red_dot)
    draw_score(world['score'])
    
################################################################################
# Dot manipulating functions

def check_dot_goal_reached(dot: RedDot):
    '''
    Tests whether the dot has reached its goal; if so, it resets to a new
    goal position.
    
    Args:
        dot (RedDot): The red dot to be testing and potentially updating.
    '''
    if is_dot_hitting_position(dot['current'], dot['goal']):
        dot['goal'] = make_random_position()
    
def move_dot(dot: RedDot):
    '''
    Moves the red dot towards its goal.
    
    Args:
        dot (RedDot): The red dot to be moving.
    '''
    angle = angle_between(dot['current'], dot['goal'])
    dot['current']['x'] += x_from_angle_speed(angle, DOT_SPEED)
    dot['current']['y'] += y_from_angle_speed(angle, DOT_SPEED)
    
################################################################################
# World manipulating functions

def update_world(world: World):
    """
    Updates the world by moving all the dots and checking if
    they've reached their goals.
    
    Args:
        world (World): The current world
    """
    for dot in world['red dots']:
        move_dot(dot)
        check_dot_goal_reached(dot)

def handle_key(world: World, key: int):
    """ Process keyboard input """

def handle_mouse(world: World, x: int, y: int, button: int):
    """ Process mouse clicks """
    
def handle_motion(world: World, x: int, y: int):
    """
    Handle the mouse moving by iterating through the red dots
    and retaining dots that are not touching the mouse. If a
    red dot is touched, it is filtered out and two new red dots
    are added instead.
    """
    kept_dots = []
    mouse_position = {'x': x, 'y': y}
    for dot in world['red dots']:
        if is_dot_hitting_position(dot['current'], mouse_position):
            # Make two new red dots
            kept_dots.append(make_red_dot())
            kept_dots.append(make_red_dot())
        else:
            # Leave dot unchanged
            kept_dots.append(dot)
    world['red dots'] = kept_dots

############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == '__main__':
    Cisc108Game(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse, handle_motion)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()
