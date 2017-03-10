# Copyright Denise van den Berg - Maes 2017

# Loading modules
import pygame, random, os, psycopg2
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#----------------------------------------------------------  LOCALS ---------------------------------------------------

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
        self.terminate = False
        self.Level = "menu"
            
    def Draw(self, image_destination): 
        self.Load = pygame.image.load(image_destination)
        self.Display.blit(self.Load, (0,0))

    def Update(self): 
        pygame.display.update()
        self.clock.tick(self.FPS)

    def Loop(self): 
        while not self.terminate:
            if self.Level == "menu": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.terminate = True 
                self.Draw("background_game_menu.jpg")
                self.Update() 
            else: self.Exit = True 

class Button:
    def __init__(self, x, y, w, h, image, constant, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load(image)
        self.constant = constant
        self.pressed = False
        self.pressing = False
        self.action = action

    def rollover(self):
        if self.x + self.w > pygame.mouse.get_pos()[0] > self.x and self.y + self.h >  pygame.mouse.get_pos()[1] > self.y:
            self.draw()

    def draw(self):
            game.Display.blit(self.image, [self.x, self.y])


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
    def SetPosition(self, number):
        self.Square = self.Square + number
# ------------------------------------------------------------------ FUNCTIONS ------------------------------------------------------------#


def terminate():
    pygame.quit()
    quit()

# ------------------------------------------------------------------ RUNNING ------------------------------------------------------------#

game = Game()
startbutton = Button(40, 325, 235, 120, "background_game_menu_button1.png", False, game.Loop())
game.Loop()
terminate()
