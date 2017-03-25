#Pygame Template - skeleton for a new pygame project
import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

#Defined Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    #keep loop running at correct speed
    clock.tick(FPS)
    #Process Inputs
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()

    #Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # * After drawing everything, flip the display *
    pygame.display.flip()


pygame.quit
quit()
