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
                dice.Draw()
                player.Draw()
                self.Update() 
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
        self.Number     = 6
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
                self.Roll()

    def Roll(self):
        self.Number = int(random.randint(1,6))

      


class Square:
    def __init__(self, color, posx, posy):
        self.Color  = color
        self.X      = posx
        self.Y      = posy

    def GetPosition(self):
        return [self.X, self.Y]

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

class Questions:
    def __init__(self, color):
        self.Color = color

        def Category():
            category = None
            if player.SetPosition == Square[1] or Square[6] or Square[11]:
                category = yellow #blit random question and make a check if correct or incorrect, add score
            if player.SetPosition == Square[2] or Square[7] or Square[12]:
                category = red 
            if player.SetPosition == Square[3] or Square[8] or Square[13]:
                category = green 
            if player.SetPosition == Square[4] or Square[9] or Square[14]:
                category = blue 
            if player.SetPosition == Square[5] or Square[10] or Square[15]:
                category = grey 
            if player.SetPosition == Square[16]:
                player = winner

                #Je 'category' functie is onnodig. Aangezien de squares de kleur zelf al in zich hebbem, je kan gew Tower.Squares[int].Color gebruiken
                #En.. Met dat positie voor de player zetten..
                #tower.Squares[int].X en tower.Squares[int].Y heb je nodig om iemand zn positie op de positie van het vak te zetten


class Player:
    def __init__(self, color):
        self.at_number = 0
        if color == "red" : self.Image = pygame.image.load("playerred.png")
        if color == "yellow" : self.Image = pygame.image.load("playeryellow.png")
        if color == "green": self.Image = pygame.image.load("playergreen.png")
        if color == "blue": self.Image = pygame.image.load("playerblue.png")

    def SetPosition(self):
        self.at_number  = self.at_number  + dice.Number

    def Draw(self): 
        game.Display.blit(self.Image, tower.Squares[self.at_number].GetPosition)

    # stel, dice.Roll gaf daadwerkelijk een cijfer terug (wat het niet doet). dan moet je het niet in de parameters doen van deze functie.
    # de parameters van de functie zijn locale variabelen voor alleen die functie. stel je noemt een parameter henk, en als je de functie oproept doe je:
    # player1.SetPosition(dice.Roll) . dan zal (in de functie) henk nu dice.Roll zijn.
    # maar aangezien je dice.Roll() gewoon kan aanroepen, hoef je het niet op te slaan als extra variabele in de functie, maar kan je het gewoon uitvoeren in de functie.

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

def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((game.Width/2),(game.Height/2))
    game.Display.blit(TextSurf, TextRect)
    game.Update()

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
tower               = Tower ()
#geen coords maar 1e cijfer = square[] en 2e = image[], doe ik dat zo goed?
#De constructor (de functie __init__ die een class uitvoert als je een instantie maakt) van class Player heeft geen parameters.
# De eerste parameter (op welke square de player begint) is altijd hetzelfde. dus hoeven wij niet aan de constructor te geven als parameter (het is altijd 0).
# Ik weet wat jij wilt, dus hier een voorbeeld (niet kopiëren plakken want dit is uitleg, geen uitwerking voor jouw probleem):

# class Player:
#     def __init__(self, welke_kleur_ben_ik):
#         self.Square = 0
#         if welke_kleur_ben_ik == "rood" : self.Image = pygame.image.load("playerred.png")
#         if welke_kleur_ben_ik == "geel" : self.Image = pygame.image.load("playerryellow.png")
#         if welke_kleur_ben_ik == "groen": self.Image = pygame.image.load("playergreen.png")
#         if welke_kleur_ben_ik == "blauw": self.Image = pygame.image.load("playerblue.png")

player1 = Player("red")
player2 = Player("yellow")
player3 = Player("green")
player4 = Player("blue")


game.Loop()
Terminate()
