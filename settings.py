# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY
SPRITESHEET = "p1_spritesheet.png"

# Gun settings
BULLET_IMG = "laserPurple.png"
BULLET_SPEED = 500
BULLET_LIFETIME = 1000

TILESIZE = 70
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
GRAVITY = .8


# Player settings
PLAYER_SPEED = 300
PLAYER_IMG = 'p1_stand.png'
PLAYER_ACC = .5
PLAYER_FRICTION = -0.12
