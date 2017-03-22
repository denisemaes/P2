# Copyright Denise van den Berg - Maes 2017

# Loading modules
import pygame, random, os, psycopg2
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#----------------------------------------------------------  LOCALS ---------------------------------------------------

# RGB Colours
Black           = (0,       0,      0)
White           = (255,     255,    255)
Red             = (200,     0,      0)
Green           = (0,       200,    0)
Blue            = (0,       0,      200)
Yellow          = (255,     204,    0)
Grey            = (192,     192,    192)

#----------------------------------------------------------- CLASSES ------------------------------------------------------

class Game:
    def __init__(self):
        self.FPS        = 30
        self.Clock      = pygame.time.Clock()
        self.Width      = 1500
        self.Height     = 750
        self.Display    = pygame.display.set_mode((self.Width, self.Height))
        self.Terminate  = False
        self.Level      = "menu"
        self.Images     = [\
                        pygame.image.load("background_game_menu.jpg"),\
                        pygame.image.load("background_empty.jpg"),\
                        pygame.image.load("background_emp2.jpg"),\
                        pygame.image.load("background_game_board.jpg"),\
                        pygame.image.load("background_winscreen.jpg"),\
                        pygame.image.load("background_emp2_instr.jpg"),\
                        pygame.image.load("background_emp2_rules.jpg")]
            

    def Draw(self, image_number): 
        self.Display.blit(self.Images[image_number], (0,0))

    def Update(self): 
        pygame.display.update()
        self.Clock.tick(self.FPS)

    def Loop(self): 
        while not self.Terminate:
            if self.Level == "menu": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(0)
                startbutton.Draw() 
                tutorialbutton.Draw()
                settingsbutton.Draw()
                highscoresbutton.Draw()
                instructionsbutton.Draw()
                rulesbutton.Draw()
                quitbutton.Draw()
                self.Update() 
            elif self.Level == "tutorial": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(2)
                quitbutton2.Draw()
                menubutton.Draw()
                self.Update() 
            elif self.Level == "settings": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(2)
                quitbutton2.Draw()
                menubutton.Draw()
                self.Update() 
            elif self.Level == "highscores": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(2)
                quitbutton2.Draw()
                menubutton.Draw()
                self.Update() 
            elif self.Level == "instructions": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(5)
                quitbutton2.Draw()
                menubutton.Draw()
                self.Update() 
            elif self.Level == "rules": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(6)
                quitbutton2.Draw()
                menubutton.Draw()
                self.Update() 
            elif self.Level == "game": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(3)
                quitbutton2.Draw()
                menubutton.Draw()
                player.Draw()
                dice.Draw()
                self.Update()
                if dice.Rolling == True:
                    #hier moet je gaan checken wat de start pos is en wat de dice roll is, setpos niet uitvoeren
                    if tower.Squares[player.at_number].GetColor() == "yellow":#bepaal kleur van de vraag
                        question.Number = int(random.randint(0,9))#bepaal nummber
                        question.Draw()
                        dice.Rolling = False 
                        player.SetPosition() 
                        self.Update()
                    elif tower.Squares[player.at_number].GetColor()  == "red":#bepaal kleur van de vraag
                        question.Number = int(random.randint(10,19))#bepaal nummber
                        question.Draw()
                        dice.Rolling = False 
                        player.SetPosition() 
                        self.Update()
                    elif tower.Squares[player.at_number].GetColor()  == "green":#bepaal kleur van de vraag
                        question.Number = int(random.randint(20,29))#bepaal nummber
                        question.Draw()
                        dice.Rolling = False 
                        player.SetPosition() 
                        self.Update()
                    elif tower.Squares[player.at_number].GetColor()  == "blue":#bepaal kleur van de vraag
                        question.Number = int(random.randint(30,39))#bepaal nummber
                        question.Draw()
                        dice.Rolling = False 
                        player.SetPosition() 
                        self.Update()
                        #bepaal of vraag goed beantwoord is
                    dice.Rolling = False #zet rolling naar false
            else: self.Terminate = True 

class Button:
    def __init__(self, x, y, w, h, image, action):
        self.X          = x
        self.Y          = y
        self.W          = w
        self.H          = h
        self.Image      = pygame.image.load(image)
        self.Pressed    = False
        self.Action     = action

    def Draw(self):
        self.Rollover()

    def Rollover(self):
        if self.X + self.W > pygame.mouse.get_pos()[0] > self.X and self.Y + self.H >  pygame.mouse.get_pos()[1] > self.Y:
            game.Display.blit(self.Image, [0, 0])
            if pygame.mouse.get_pressed()[0] == True:
                self.Pressed = True
            elif self.Pressed == True:
                self.Action()
                self.Pressed = False
        
class Dice: 
    def __init__(self, x, y, h, w):
        self.X          = x
        self.Y          = y
        self.H          = h
        self.W          = w
        self.Rolling    = False
        self.Number     = 0
        self.Images     =[\
                        pygame.image.load("diceroll.png"),\
                        pygame.image.load("dice1.png"),\
                        pygame.image.load("dice2.png"),\
                        pygame.image.load("dice3.png"),\
                        pygame.image.load("dice4.png"),\
                        pygame.image.load("dice5.png"),\
                        pygame.image.load("dice6.png")]
        
   
    def Draw(self):
        self.Rollover()
        game.Display.blit(self.Images[self.Number], (self.X, self.Y))


    def Rollover(self): 
        if self.X + self.W > pygame.mouse.get_pos()[0] > self.X and self.Y + self.H >  pygame.mouse.get_pos()[1] > self.Y:
            game.Display.blit(self.Images [0], (self.X, self.Y))
            if pygame.mouse.get_pressed()[0] == True:
                self.Rolling = True
                self.Roll()
                self.Rolling = False

    def Roll(self):
        self.Number = int(random.randint(1,6))
        return [self.Number]
    

class Square:
    def __init__(self, color, posx, posy):
        self.Color  = color
        self.X      = posx
        self.Y      = posy

    def GetPosition(self):
        return [self.X, self.Y]

    def GetColor(self):
        return [self.Color]

class Tower:
    def __init__(self):
        self.Squares = [\
            Square("start",   1260, 725),\
            Square("yellow",  1260, 700),\
            Square("red",     1260, 680),\
            Square("green",   1260, 660),\
            Square("blue",    1260, 635),\
            Square("grey",    1260, 605),\
            Square("yellow",  1260, 560),\
            Square("red",     1260, 500),\
            Square("green",   1260, 450),\
            Square("blue",    1260, 390),\
            Square("grey",    1260, 230),\
            Square("yellow",  1260, 220),\
            Square("red",     1262, 175),\
            Square("green",   1265, 130),\
            Square("blue",    1270, 100),\
            Square("grey",    1280, 60 ),\
            Square("win",     1290, 25 )]

class Question:
    def __init__(self, x, y, w, h):
        self.X          = x
        self.Y          = y
        self.W          = w
        self.H          = h
        self.Number     = 0
        self.Images     = [\
                        pygame.image.load("QR1.png"),\
                        pygame.image.load("QR2.png"),\
                        pygame.image.load("QR3.png"),\
                        pygame.image.load("QR4.png"),\
                        pygame.image.load("QR5.png"),\
                        pygame.image.load("QR6.png"),\
                        pygame.image.load("QR7.png"),\
                        pygame.image.load("QR8.png"),\
                        pygame.image.load("QR9.png"),\
                        pygame.image.load("QR10.png"),\
                        pygame.image.load("QY1.png"),\
                        pygame.image.load("QY2.png"),\
                        pygame.image.load("QY3.png"),\
                        pygame.image.load("QY4.png"),\
                        pygame.image.load("QY5.png"),\
                        pygame.image.load("QY6.png"),\
                        pygame.image.load("QY7.png"),\
                        pygame.image.load("QY8.png"),\
                        pygame.image.load("QY9.png"),\
                        pygame.image.load("QY10.png"),\
                        pygame.image.load("QG1.png"),\
                        pygame.image.load("QG2.png"),\
                        pygame.image.load("QG3.png"),\
                        pygame.image.load("QG4.png"),\
                        pygame.image.load("QG5.png"),\
                        pygame.image.load("QG6.png"),\
                        pygame.image.load("QG7.png"),\
                        pygame.image.load("QG8.png"),\
                        pygame.image.load("QG9.png"),\
                        pygame.image.load("QG10.png"),\
                        pygame.image.load("QB1.png"),\
                        pygame.image.load("QB2.png"),\
                        pygame.image.load("QB3.png"),\
                        pygame.image.load("QB4.png"),\
                        pygame.image.load("QB5.png"),\
                        pygame.image.load("QB6.png"),\
                        pygame.image.load("QB7.png"),\
                        pygame.image.load("QB8.png"),\
                        pygame.image.load("QB9.png"),\
                        pygame.image.load("QB10.png")]

        def Draw(self):
            game.Display.blit(self.Images[self.Number], (self.X, self.Y))



class Player:
    def __init__(self, color):
        self.at_number = 0
        if color == "red"       : self.Image = pygame.image.load("playerred.png")
        if color == "yellow"    : self.Image = pygame.image.load("playeryellow.png")
        if color == "green"     : self.Image = pygame.image.load("playergreen.png")
        if color == "blue"      : self.Image = pygame.image.load("playerblue.png")

    def SetPosition(self):
        self.at_number  = self.at_number + dice.Number
        print(self.at_number)

    def Draw(self): 
        game.Display.blit(self.Image, tower.Squares[self.at_number].GetPosition())


# ------------------------------------------------------------------ FUNCTIONS ------------------------------------------------------------#

def startgame():
    game.Level = "game"

def starttutorial():
    game.Level = "tutorial"

def startsettings():
    game.Level = "settings"

def starthighscores():
    game.Level = "highscores"

def startinstructions():
    game.Level = "instructions"

def startrules():
    game.Level = "rules"

def startmenu():
    game.Level = "menu"



def Terminate():
    pygame.quit()
    quit()

# ------------------------------------------------------------------ RUNNING ------------------------------------------------------------#

game                = Game()
startbutton         = Button(40,    325,    235,    120,    "background_game_menu_button1.png", startgame) 
tutorialbutton      = Button(900,   350,    320,    120,    "background_game_menu_button2.png", starttutorial) 
settingsbutton      = Button(1330,  20,     150,    60,     "background_game_menu_button3.png", startsettings) 
highscoresbutton    = Button(1330,  135,    150,    60,     "background_game_menu_button4.png", starthighscores) 
instructionsbutton  = Button(7,     455,    155,    90,     "background_game_menu_button5.png", startinstructions) 
rulesbutton         = Button(170,   500,    150,    90,     "background_game_menu_button6.png", startrules) 
quitbutton          = Button(1380,  590,    100,    50,     "background_game_menu_button7.png", Terminate) 
quitbutton2         = Button(1380,  670,    100,    50,     "background_emp2_button8.png",      Terminate) 
menubutton          = Button(20,    670,    100,    50,     "background_emp2_button9.png",      startmenu) 
dice                = Dice  (270,   210,    116,    116)
question            = Question(470, 80, 305, 380)
tower               = Tower ()
player              = Player("red")
#player1             = Player("red")
#player2             = Player("yellow")
#player3             = Player("green")
#player4             = Player("blue")
game.Loop()
Terminate()
