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
                        #oproepen self.Images[0]
            

    def Draw(self, image_number): 
        self.Display.blit(self.Images[image_number], (0,0))

    def DrawObjects(self, *list_of_objects):
       for obj in list_of_objects:
            obj.Draw()

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
                self.DrawObjects(startbutton, tutorialbutton, settingsbutton, highscoresbutton, instructionsbutton, rulesbutton, quitbutton)
                self.Update() 
            elif self.Level == "tutorial": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(2)
                self.DrawObjects(quitbutton2, menubutton)
                self.Update() 
            elif self.Level == "settings": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(2)
                self.DrawObjects(quitbutton2, menubutton)
                self.Update() 
            elif self.Level == "highscores": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(2)
                self.DrawObjects(quitbutton2, menubutton)
                self.Update() 
            elif self.Level == "instructions": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(5)
                self.DrawObjects(quitbutton2, menubutton)
                self.Update() 
            elif self.Level == "rules": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(6)
                self.DrawObjects(quitbutton2, menubutton)
                self.Update() 
            elif self.Level == "game": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(3)
                self.DrawObjects(quitbutton2, menubutton, dice)
                self.Update() 
            else: self.Terminate = True 

class Button:
    def __init__(self, x, y, w, h, image, constant, action):
        self.X          = x
        self.Y          = y
        self.W          = w
        self.H          = h
        self.Image      = pygame.image.load(image)
        self.Constant   = constant
        self.Pressed    = False
        self.Pressing   = False
        self.Action     = action

    def Draw(self):
        self.Rollover()

    def Rollover(self):
        if self.X + self.W > pygame.mouse.get_pos()[0] > self.X and self.Y + self.H >  pygame.mouse.get_pos()[1] > self.Y:
            game.Display.blit(self.Image, [0, 0])
            if pygame.mouse.get_pressed()[0] == True:
                self.Action()

class Dice:
    def __init__(self):
        # dus de dice heeft alleen fotos. niks anders?
        # geen xcoordinaat, ycoordinaat, nummer, etc..? je gebruikt ze anders wel in een functie terwijl ze nog niet bestaan?
        self.Images     =[\
                        pygame.image.load("dice1.png"),\
                        pygame.image.load("dice2.png"),\
                        pygame.image.load("dice3.png"),\
                        pygame.image.load("dice4.png"),\
                        pygame.image.load("dice5.png"),\
                        pygame.image.load("dice6.png"),\
                        pygame.image.load("diceroll.png")]
    
    def Draw(self):
        self.Rollover()

    def Rollover(self):
        # je gebruikt variabelen die (nog) niet bestaan.
        if self.X + self.W > pygame.mouse.get_pos()[0] > self.X and self.Y + self.H >  pygame.mouse.get_pos()[1] > self.Y:
            game.Display.blit(self.Images[6], (270, 210))
            if pygame.mouse.get_pressed()[0] == True:
                self.Roll()
                
    def Roll(self):
        # je gebruikt variabelen die (nog) niet bestaan.
        self.Number = random.randint(1,6)
        # dit verandert alleen het nummer van de dice (self.Number).
        # dit is wat je dus gebruikt als je het cijfertje wilt veranderen en dus ALLEEN voor dat.
        # niet gebruiken voor een cijfer krijgen zoals je in een player functie probeerde. dit slaat nergens op.

    def Draw(self, image_number): 
        # je gebruikt variabelen die (nog) niet bestaan.
        # het is game.Display.blit . niet Display.blit .
        # waarom doe je self.Images[getal, (getal, getal)] ? dit klopt niet.
        # om een array element te gebruiken doe je self.Images[INTEGER] . de coordinaten horen NIET in de verwijzing naar een element van de array.
        if   self.Number == 1: Display.blit(self.Images[0, (270, 210)])
        elif self.Number == 2: Display.blit(self.Images[1, (270, 210)])
        elif self.Number == 3: Display.blit(self.Images[2, (270, 210)])
        elif self.Number == 4: Display.blit(self.Images[3, (270, 210)])
        elif self.Number == 5: Display.blit(self.Images[4, (270, 210)])
        elif self.Number == 6: Display.blit(self.Images[5, (270, 210)])

        # dus je gaat non-stop deze text laten zien? zo ja prima.
        message_display("You rolled: " + str(Roll)) # Wat is Roll? het bestaat niet.

class Square:
    def __init__(self, color, posx, posy):
        self.Color  = color
        self.X      = posx
        self.Y      = posy

class Tower:
    def __init__(self):
        self.Square = [\
            Square(start,   1260, 725),\
            Square(yellow,  1260, 700),\
            Square(red,     1260, 680),\
            Square(green,   1260, 660),\
            Square(blue,    1260, 635),\
            Square(grey,    1260, 605),\
            Square(yellow,  1260, 560),\
            Square(red,     1260, 500),\
            Square(green,   1260, 450),\
            Square(blue,    1260, 390),\
            Square(grey,    1260, 230),\
            Square(yellow,  1260, 220),\
            Square(red,     1262, 175),\
            Square(green,   1265, 130),\
            Square(blue,    1270, 100),\
            Square(grey,    1280, 60 ),\
            Square(win,     1290, 25 )]

class Player:
    def __init__(self):
        self.Square = 0
        self.Images =[\
            pygame.image.load("playerred.png"),\
            pygame.image.load("playeryellow.png"),\
            pygame.image.load("playergreen.png"),\
            pygame.image.load("playerblue.png")]

    # stel, dice.Roll gaf daadwerkelijk een cijfer terug (wat het niet doet). dan moet je het niet in de parameters doen van deze functie.
    # de parameters van de functie zijn locale variabelen voor alleen die functie. stel je noemt een parameter henk, en als je de functie oproept doe je:
    # player1.SetPosition(dice.Roll) . dan zal (in de functie) henk nu dice.Roll zijn.
    # maar aangezien je dice.Roll() gewoon kan aanroepen, hoef je het niet op te slaan als extra variabele in de functie, maar kan je het gewoon uitvoeren in de functie.
    def SetPosition(self, dice.Roll):
        Square() = Square() + dice.Roll()

    def Draw(self, image_number): 
        self.Display.blit(self.Images[image_number], (Square()))

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

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    game.Display.blit(TextSurf, TextRect)
    game.Display.Update()

def Terminate():
    pygame.quit()
    quit()

# ------------------------------------------------------------------ RUNNING ------------------------------------------------------------#

game                = Game()
startbutton         = Button(40,    325,    235,    120,    "background_game_menu_button1.png", False, startgame) 
tutorialbutton      = Button(900,   350,    320,    120,    "background_game_menu_button2.png", False, starttutorial) 
settingsbutton      = Button(1330,  20,     150,    60,     "background_game_menu_button3.png", False, startsettings) 
highscoresbutton    = Button(1330,  135,    150,    60,     "background_game_menu_button4.png", False, starthighscores) 
instructionsbutton  = Button(7,     455,    155,    90,     "background_game_menu_button5.png", False, startinstructions) 
rulesbutton         = Button(170,   500,    150,    90,     "background_game_menu_button6.png", False, startrules) 
quitbutton          = Button(1380,  590,    100,    50,     "background_game_menu_button7.png", False, Terminate) 
quitbutton2         = Button(1380,  670,    100,    50,     "background_emp2_button8.png",      False, Terminate) 
menubutton          = Button(20,    670,    100,    50,     "background_emp2_button9.png",      False, startmenu) 
dice                = Dice()

player1             = Player(0,0) #geen coords maar 1e cijfer = square[] en 2e = image[], doe ik dat zo goed?

# De constructor (de functie __init__ die een class uitvoert als je een instantie maakt) van class Player heeft geen parameters.
# De eerste parameter (op welke square de player begint) is altijd hetzelfde. dus hoeven wij niet aan de constructor te geven als parameter (het is altijd 0).
# Ik weet wat jij wilt, dus hier een voorbeeld (niet kopiëren plakken want dit is uitleg, geen uitwerking voor jouw probleem):

# class Player:
#     def __init__(self, welke_kleur_ben_ik):
#         self.Square = 0
#         if welke_kleur_ben_ik == "rood" : self.Image = pygame.image.load("playerred.png")
#         if welke_kleur_ben_ik == "geel" : self.Image = pygame.image.load("playerryellow.png")
#         if welke_kleur_ben_ik == "groen": self.Image = pygame.image.load("playergreen.png")
#         if welke_kleur_ben_ik == "blauw": self.Image = pygame.image.load("playerblue.png")

# player1 = Player("rood")
# player2 = Player("geel")
# player3 = Player("groen")
# player4 = Player("blauw")

# Ik hoop dat ik hiermee verduidelijk dat je moet nadenken en niet blindelings dingen kopiëert van een class die eerder gemaakt is.
        

player2             = Player(0,1)
player3             = Player(0,2)
player4             = Player(0,3)
game.Loop()
Terminate()
