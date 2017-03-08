# Copyright Denise van den Berg - Maes 2017

# Loading modules
import pygame, random, os, psycopg2
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#--------------------------------------------------------------  LOCALS ---------------------------------------------------

# RGB Colours
Black           = (0,0,0)
White           = (255,255,255)
Red             = (200,0,0)
Green           = (0,200,0)
Blue            = (0, 0, 200)
Yellow          = (255, 204, 0)
Grey            = (192,192,192)

#----------------------------------------------------------- CLASSES ------------------------------------------------------

class Game:
    def __init__(self):
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.Width = 1500
        self.Height = 750
        self.Display = pygame.display.set_mode((self.Width, self.Height))
        self.Exit = False
        self.Level = "menu"
            
    def Draw(self): 
        self.Display.blit(pygame.image.load(), [0, 0])

    def Update(self): 
        pygame.display.update()
        self.clock.tick(self.FPS)

    def Loop(self): 
        while not self.Exit:
            if self.Level == "menu": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Exit = True 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.Exit = True
                self.Draw("background_game_menu.jpg")
                self.Tick() # refreshes the window. this is the end of the loop
            # you can use elifs here to make new levels
            else: self.Exit = True 

class Button:
    def __init__(self, x, y, w, h, constant):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.constant = constant

    def draw():
        self.Display.blit(pygame.image.load(), [0, 0])
    def click():
        for event in pygame.event.get():
            if event.type == pygame.mouse.get_pressed():
                pos = pygame.mouse.get_pos()
                if self.collidepoint(pos):
                    return

class Square:
    def __init__(self, color, posx, posy):
        self.Color = color
        self.X = posx
        self.Y = posy

class Tower:
    def __init__(self):
        self.Square = [\
            Square(start, 1260, 725),\
            Square(yellow, 1260, 700),\
            Square(red, 1260, 680),\
            Square(green, 1260, 660),\
            Square(blue, 1260, 635),\
            Square(grey, 1260, 605),\
            Square(yellow, 1260, 560),\
            Square(red, 1260, 500),\
            Square(green, 1260, 450),\
            Square(blue, 1260, 390),\
            Square(grey, 1260, 230),\
            Square(yellow, 1260, 220),\
            Square(red, 1262, 175),\
            Square(green, 1265, 130),\
            Square(blue, 1270, 100),\
            Square(grey, 1280, 60),\
            Square(win, 1290, 25)]

class Player:
    def __init__(self):
        self.Square = 0
        self.image = image
    def SetPosition(self):
        self.Square = self.Square + Dice.Roll

class Dice:
    def __init__(self, x, y, player):
        self.X = x
        self.Y = y
        self.Player = player
        self.Image = image
    
    def Roll(self):
        self.Number = random.randint(1,6)
    
    def Draw(self):
        # getting the 'code' for the eyes that have to be drawn
        if   self.Number == 1: self.Image = pygame.image.load(("dice1.png"), [270, 210])
        elif self.Number == 2: self.Image = pygame.image.load(("dice2.png"), [270, 210])
        elif self.Number == 3: self.Image = pygame.image.load(("dice3.png"), [270, 210])
        elif self.Number == 4: self.Image = pygame.image.load(("dice4.png"), [270, 210])
        elif self.Number == 5: self.Image = pygame.image.load(("dice4.png"), [270, 210])
        elif self.Number == 6: self.Image = pygame.image.load(("dice5.png"), [270, 210])


game = Game()
game.Loop()
pygame.quit()
quit()