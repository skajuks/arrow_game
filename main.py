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
        self.dt = self.clock.tick()
        self.time += self.dt
        count = 0
        for row in self.grows:
            if row.id == 2:
                pass
        missedcount = 0    
        for arrow in self.arrows:
            arrow.rect.x -=3
            if arrow.rect.x < 0:
                if arrow.status == 'not hit':
                    print("missed", " : ", missedcount)
                    missedcount +=1
                arrow.kill() 
        print(self.time)
        if self.randintcreate == True:
            self.integer = randint(50,400)
            self.randintcreate = False
        if self.time > self.integer:
            self.activate_new_arrow = True
            self.time = 0
            self.randintcreate = True               

        hitboxcol = pg.sprite.spritecollide(self.check_col_box, self.arrows, False)   
        if hitboxcol:
            closest = hitboxcol[0]
            for hit in hitboxcol: 
                if hit.status == 'not_hit': #hit.rect.left <= closest.rect.left and
                    if hit.id == 1 and self.up == True:
                        closest = hit
                        closest.status = 'hit'
                        
                    elif hit.id == 2 and self.right == True:
                        closest = hit
                        closest.status = 'hit'
                        
                    elif hit.id == 3 and self.left == True:
                        closest = hit
                        closest.status = 'hit'
              
                    elif hit.id == 4 and self.down == True:
                        closest = hit
                        closest.status = 'hit'
       
                    #print('HIT', ':', hit.id)
                    #closest = hit

  

    def new(self):
        pg.init()
        self.time = 0
        self.integer = 100
        self.randintcreate = True
        self.activate_new_arrow = False
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.grows = pg.sprite.Group()
        self.arrows = pg.sprite.Group()
        self.hitboxes = pg.sprite.Group()
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        maximum_row_h = PLAYFIELD_HEIGHT // 4
        maximum_row_h_max =-maximum_row_h
        colorlist = [RED, YELLOW, GREEN, BLUE]
        x = 0
        y = 0
        rowid = 1
        for row in self.rows:
            if x >= maximum_row_h_max:
                Mainboard_Row(self, x, colorlist[y], rowid)
                x +=maximum_row_h
                y+=1
                rowid +=1     
        self.check_col_box = HitBox(self, 100, maximum_row_h * 4, 150, WHITE) 
        HitBox(self, self.check_col_box.rect.centerx - 5, maximum_row_h * 4, 10, BLACK) 

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
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.up = False
                if event.key == pg.K_DOWN:
                    self.down = False
                if event.key == pg.K_RIGHT:
                    self.right = False
                if event.key == pg.K_LEFT:
                    self.left = False                   
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
