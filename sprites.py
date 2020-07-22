from settings import *
import pygame as pg
from random import choice, randrange, randint
from os import path
import time

vc = pg.math.Vector2


class Spritesheet:
    # utility for images
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def bg(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Mainboard_Row(pg.sprite.Sprite):
    def __init__(self, game, pos, c, rowid):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.grows
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.id = rowid
        self.image = pg.Surface((WIDTH, 10))
        self.image.fill(c)
        self.rect = self.image.get_rect()
        self.rect.y = pos
        self.randintcreate = True
        self.integer = 100

    def update(self):
        if self.game.activate_new_arrow == True:
            Arrow(self.game, self.id, self) 
            self.game.activate_new_arrow = False
              
class HitBox(pg.sprite.Sprite):
    def __init__(self, game, x,y,h,color):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.hitboxes
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game    
        self.image = pg.Surface((h, int(round(y))))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            print("hit GREEN")
            self.image.fill(VIOLET)
        else:
            self.image.fill(WHITE)        
class Arrow(pg.sprite.Sprite):
    def __init__(self, game, ids, line):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.arrows
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.status = 'not_hit'
        self.id = ids
        self.line = line
        if self.id == 1:
            self.image = pg.image.load(path.join(self.game.img_dir, "red_arrow.png"))
            self.rect = self.image.get_rect()
            self.rect.y = self.line.rect.y + 60
            self.rect.x = WIDTH + 30   
        elif self.id == 2:
            self.image = pg.image.load(path.join(self.game.img_dir, "yellow_arrow.png"))
            self.rect = self.image.get_rect()
            self.rect.y = self.line.rect.y + 60
            self.rect.x = WIDTH + 30  
        elif self.id == 3:
            self.image = pg.image.load(path.join(self.game.img_dir, "green_arrow.png"))
            self.rect = self.image.get_rect()
            self.rect.y = self.line.rect.y + 60 
            self.rect.x = WIDTH + 30  
        elif self.id == 4: 
            self.image = pg.image.load(path.join(self.game.img_dir, "blue_arrow.png"))
            self.rect = self.image.get_rect()
            self.rect.y = self.line.rect.y + 60
            self.rect.x = WIDTH + 30           
    def update(self):
        if self.status == 'hit':
            self.image.fill(HIT)        