from settings import *
import pygame as pg
import math, random, sys, time
from sprites import *


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.clock = pg.time.Clock()
        self.MAINWINDOW = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(gameTitle)
        self.load_data()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.rows = [1,2,3,4]

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw()

    def update(self):
        self.all_sprites.update()
        for row in self.grows:
            if row.id == 2:
                pass
        for block in self.holdblocks:
            if block.freeze == False:
                block.rect.x -=10
            if block.rect.right < 0:
                block.kill()    

        for arrow in self.arrows:
            if len(self.arrows) > 0:
                #print(arrow.rect.x)
                arrow.rect.x -=10
                if arrow.rect.right < 0:
                    #print(arrow.status)
                    if arrow.status == 'not_hit':
                        print("missed : ", self.missedcount)
                        self.missedcount +=1
                    arrow.kill() 
       # print(self.time)
        if self.randintcreate == True:
            self.integer = randint(50,400)
            self.randintcreate = False
        if self.time > self.integer:
            self.activate_new_arrow = True
            self.time = 0
            self.randintcreate = True                 
        holdboxcol = pg.sprite.spritecollide(self.check_col_box, self.holdblocks, False)
        if holdboxcol:
            for hit in holdboxcol:
                if hit.hold.id == 1 and self.a == True:
                    hit.color = VIOLET
                    hit.freeze = True
                    if hit.hold.rect.right <= hit.rect.centerx or self.a == False:
                        hit.freeze = False 
                    if hit.hold.rect.right <= hit.rect.centerx:
                        hit.color = GREEN
                        hit.hold.status = 'hit'
                elif hit.hold.id == 2 and self.s == True:
                    hit.color = VIOLET
                    hit.freeze = True
                    if hit.hold.rect.right <= hit.rect.centerx or self.s == False:
                        hit.freeze = False
                    if hit.hold.rect.right <= hit.rect.centerx:
                        hit.color = GREEN
                        hit.hold.status = 'hit'
                elif hit.hold.id == 3 and self.d == True:
                    hit.color = VIOLET
                    hit.freeze = True
                    if hit.hold.rect.right <= hit.rect.centerx or self.d == False:
                        hit.freeze = False
                    if hit.hold.rect.right <= hit.rect.centerx:
                        hit.color = GREEN  
                        hit.hold.status = 'hit'                      
                elif hit.hold.id == 4 and self.f == True:
                    hit.color = VIOLET
                    hit.freeze = True
                    if hit.hold.rect.right <= hit.rect.centerx or self.f == False:
                        hit.freeze = False  
                    if hit.hold.rect.right <= hit.rect.centerx:
                        hit.color = GREEN 
                        hit.hold.status = 'hit'                        
                else:
                    hit.freeze = False                             
        hitboxcol = pg.sprite.spritecollide(self.check_col_box, self.arrows, False)   
        if hitboxcol:
            closest = hitboxcol[0]
            for hit in hitboxcol: 
                if hit.status == 'not_hit': #hit.rect.left <= closest.rect.left and
                    if hit.id == 1 and self.up == True and hit.type == 'arrow':
                            
                        closest = hit
                        closest.status = 'hit'
                        
                    elif hit.id == 2 and self.right == True and hit.type == 'arrow':
                        closest = hit
                        closest.status = 'hit'
                        
                    elif hit.id == 3 and self.left == True and hit.type == 'arrow':
                        closest = hit
                        closest.status = 'hit'
              
                    elif hit.id == 4 and self.down == True and hit.type == 'arrow':
                        closest = hit
                        closest.status = 'hit'

    def new(self):
        pg.init()
        self.time = 0
        self.integer = 100
        self.missedcount = 0
        self.randintcreate = True
        self.activate_new_arrow = False
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.grows = pg.sprite.Group()
        self.arrows = pg.sprite.Group()
        self.hitboxes = pg.sprite.Group()
        self.holdblocks = pg.sprite.Group()
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.a = False
        self.s = False
        self.d = False
        self.f = False
        maximum_row_h = PLAYFIELD_HEIGHT // 4
        maximum_row_h_max =-maximum_row_h
        x = 0
        rowid = 1
        for row in self.rows:
            if x >= maximum_row_h_max:
                Mainboard_Row(self, x, GUITAR_NECK, rowid)
                x +=maximum_row_h
                rowid +=1     
        self.check_col_box = HitBox(self, 100, maximum_row_h * 4, 150, ALPHA) 
        HitBox(self, self.check_col_box.rect.centerx - 5, maximum_row_h * 4, 10, WHITE) 

        g.run()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                for s in self.hitboxes:
                    s.check_click(event.pos)    
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.up = True
                if event.key == pg.K_DOWN:
                    self.down = True
                if event.key == pg.K_RIGHT:
                    self.right = True
                if event.key == pg.K_LEFT:
                    self.left = True
                if event.key == pg.K_a:
                    self.a = True  
                if event.key == pg.K_s:
                    self.s = True                   
                if event.key == pg.K_d:
                    self.d = True                   
                if event.key == pg.K_f: 
                    self.f = True                              # god help me for this
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.up = False
                if event.key == pg.K_DOWN:
                    self.down = False
                if event.key == pg.K_RIGHT:
                    self.right = False
                if event.key == pg.K_LEFT:
                    self.left = False
                if event.key == pg.K_a:
                    self.a = False  
                if event.key == pg.K_s:
                    self.s = False                  
                if event.key == pg.K_d:
                    self.d = False                   
                if event.key == pg.K_f: 
                    self.f = False                      

    def draw(self):
        self.MAINWINDOW.fill(BCG)

        self.all_sprites.draw(self.MAINWINDOW)
        pg.display.flip()

    def waitForKey(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP or event.type == pg.MOUSEBUTTONDOWN:
                    waiting = False

    def load_data(self):
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, "textures")
        
g = Game()

while g.running:
    g.new()


pg.quit()
