import pygame as pg
from settings import *
vec = pg.math.Vector2
class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self , x, y, width, height):
        #grab an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames = self.game.spritesheet.get_image(67, 196, 66, 92)
        self.standing_frames.set_colorkey(BLACK)
        self.walking_frames_r = [self.game.spritesheet.get_image(0, 0, 72, 97),
                                  self.game.spritesheet.get_image(73, 0, 72, 97),
                                  self.game.spritesheet.get_image(146, 0, 72, 97),
                                  self.game.spritesheet.get_image(0,98, 72, 97),
                                  self.game.spritesheet.get_image(146, 98, 72, 97),
                                  self.game.spritesheet.get_image(219, 0, 72, 97),
                                  self.game.spritesheet.get_image(292, 0, 72, 97),
                                  self.game.spritesheet.get_image(219, 98, 72, 97),
                                  self.game.spritesheet.get_image(365, 0, 72, 97),
                                  self.game.spritesheet.get_image(292, 98, 72, 97)]
        for frame in self.walking_frames_r:
            frame.set_colorkey(BLACK)
        self.walking_frames_l = []
        for frame in self.walking_frames_r:
            frame.set_colorkey(BLACK)
            self.walking_frames_l.append(pg.transform.flip(frame, True, False))
        self.jump_frame = self.game.spritesheet.get_image(438, 93, 67, 94)
        self.jump_frame.set_colorkey(BLACK)


    '''
    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

            '''

    def collide_with_obstacles(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.plats, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.plats, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def collide_with_plats(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.plats, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.plats, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y


    def jump(self):

        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.plats, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -25




    def update(self):
        '''
        self.get_keys()
        self.pos += self.vel * self.game.dt
        '''
        self.animate()
        self.acc = vec(0, GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        if self.acc.x == 0:
            self.vel.x = 0

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.x = self.pos.x
        self.collide_with_plats('x')
        self.rect.y = self.pos.y
        self.collide_with_plats('y')

        #self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        current_vely = self.vel[1]
        current_velx = self.vel[0]

        if current_vely != 0.0:
            self.jumping = True
        else:
            self.jumping = False

        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # Show Walking Animation
        if self.walking:
            if now - self.last_update > 50:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walking_frames_r[self.current_frame]
                else:
                    self.image = self.walking_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.jumping and current_velx > 0:
            self.image = self.jump_frame
        if self.jumping and current_velx < 0:
            self.image = pg.transform.flip(self.jump_frame, True, False)


        if not self.jumping and not self.walking:
                self.image = self.standing_frames


class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.plats
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.plats
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((w, h))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
