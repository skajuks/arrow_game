from settings import *
import pygame as pg
from random import choice, randrange, randint
from os import path
import time

class Mainboard_Row(pg.sprite.Sprite):
    def __init__(self, game, pos, c, rowid):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.grows
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.id = rowid
        self.image = pg.Surface((WIDTH, 110))
        self.image.fill(c)
        self.rect = self.image.get_rect()
        self.rect.y = pos
        self.timer = 0
        self.enable_timer = True
        self.intt = 0
        Mainboard_Row_Border(self.game, self)

    def update(self):
        if self.enable_timer == True:
            self.intt = randint(40,200)
            self.enable_timer = False    
        if self.timer > self.intt:
            if randint(1,8) == 4:
                Arrow(self.game, self.id, self, 'hold', randint(400,1000))
            else:
                #pass
                Arrow(self.game, self.id, self, 'arrow', 0)
            self.game.note_counter +=1
            print("notes : ", self.game.note_counter, " hit notes : ", self.game.hit_note_counter)        
            self.timer = 0
            self.enable_timer = True 
        self.timer +=1
class Mainboard_Row_Border(pg.sprite.Sprite):
    def __init__(self, game, parent):
        self._layer = P_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.parent = parent
       # self.parent = parent
        self.image = pg.Surface((WIDTH, 5))
        self.image.fill(GUITAR_NECK_B)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.parent.rect.bottom
              
class HitBox(pg.sprite.Sprite):
    def __init__(self, game, x,y,h,color):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.hitboxes
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game    
        self.image = pg.Surface((h, int(round(y)))).convert_alpha()
        if color[-1] == 128:
            self.image.fill(color, None, pg.BLEND_RGBA_MULT)
        else:  
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
    def __init__(self, game, ids, line, typea, hold_lenght):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.arrows
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.status = 'not_hit'
        self.type = typea
        self.id = ids
        self.holdlenght = hold_lenght
        self.line = line
        self.imglist = ["red_arrow.png", "yellow_arrow.png", "green_arrow.png","blue_arrow.png" ]
        if self.type == 'arrow':
            for x in range(5):
                if self.id == x:
                    self.image = pg.image.load(path.join(self.game.img_dir, self.imglist[x - 1]))  
                    self.image = pg.transform.scale(self.image, (90, 90))  
                    self.rect = self.image.get_rect()
                    self.rect.centery = self.line.rect.centery
                    self.rect.x = WIDTH + 30   
            
        if self.type == 'hold':
            for x in range(5):
                if self.id == x:
                    self.image = pg.Surface((self.holdlenght, 20))
                    self.image.fill(BLACK)
                    self.rect = self.image.get_rect()
                    self.rect.centery = self.line.rect.centery
                    self.rect.x = WIDTH + 30
                    HoldBlocksNr(self.game, self, RED)
                           
    def update(self):
        if self.status == 'hit':
            self.image.fill(HIT)
            
class HoldBlocksNr(pg.sprite.Sprite):
    def __init__(self, game, hold, color):
        self._layer = P_LAYER
        self.groups = game.all_sprites, game.holdblocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.hold = hold
        self.color = color
        if self.hold.id == 1:
            self.image = pg.image.load(path.join(self.game.img_dir, "a.png"))
        elif self.hold.id == 2:
            self.image = pg.image.load(path.join(self.game.img_dir, "s.png"))    
        elif self.hold.id == 3:
            self.image = pg.image.load(path.join(self.game.img_dir, "d.png")) 
        elif self.hold.id == 4:
            self.image = pg.image.load(path.join(self.game.img_dir, "f.png"))                     
        self.rect = self.image.get_rect()
        self.rect.center = self.hold.rect.midleft
        
        self.freeze = False
    def update(self):
        pass
        #if self.hold.id != 1 or self.hold.id != 2 :
           #self.image.fill(self.color)         
