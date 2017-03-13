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
        self.Clock = pygame.time.Clock()
        self.Width = 1500
        self.Height = 750
        self.Display = pygame.display.set_mode((self.Width, self.Height))
        self.Terminate = False
        self.Level = "menu"
            
    def Draw(self, image_destination): 
        self.Load = pygame.image.load(image_destination)
        self.Display.blit(self.Load, (0,0))
        #fix dit, niet elke keer laden  >> Geen idee hoe?

    def Update(self): 
        pygame.display.update()
        self.Clock.tick(self.FPS)

    def Loop(self): 
        while not self.Terminate:
            if self.Level == "menu": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw("background_game_menu.jpg")
                startbutton.Draw() ##Start button niet defined??????
                self.Update() 
            else: self.Terminate = True 

class Button:
    def __init__(self, x, y, w, h, image, constant, action):
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.Image = pygame.image.load(image)
        self.Constant = constant
        self.Pressed = False
        self.Pressing = False
        self.Action = action

    def Draw(self):
        # op dit moment wordt de knop altijd getekent. zorg ervoor dat er getekent wordt als de muis er overheen gaat. >> Geen idee hoe.
        game.Display.blit(self.image, [0, 0]) # positie [0, 0], want kijk naar de images die je gebruikt. de button is niet rechtsbovenin getekent.   << Got it. Maar als dat wel het geval zou zijn dan wel zoals eerst?

    def Rollover(self):
        if self.X + self.W > pygame.mouse.get_pos()[0] > self.X and self.Y + self.H >  pygame.mouse.get_pos()[1] > self.Y:
            self.Draw() 
            # dit is een verkeerde manier van programmeren. aangezien de draw functie iedere keer uitgevoert wordt, en niet rollover.   >>> Waarom is dat fout?
            # stel je voert rollover uit in de draw functie, dan zou er infinite recursion komen als de if in rollover true is.   >>>> Is dat een slecht iets of een goed iets?? 




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
        self.Image = image
    def SetPosition(self, number):
        self.Square = self.Square + number
# ------------------------------------------------------------------ FUNCTIONS ------------------------------------------------------------#


def Terminate():
    pygame.quit()
    quit()

# ------------------------------------------------------------------ RUNNING ------------------------------------------------------------#

game = Game()
game.Loop()
startbutton = Button(40, 325, 235, 120, "background_game_menu_button1.png", False, game.Level == 'exit') #Dit was om puur iets erin te hebben, is dit beter? Zodat die straks naar ander level kan?
Terminate()
