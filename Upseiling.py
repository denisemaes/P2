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

class Question:
    def __init__(self, q, a, posx, posy):
        self.Q          = q
        self.A          = a
        self.Posx       = x
        self.Posx       = y
        self.Color      = tower.Squares[0].Color 
        self.atNumber   = 0
        if self.Color   == 'red': 
            self.Number = int(random.randint(0,9))
        if self.Color   == 'yellow':
            self.Number = int(random.randint(10,19))
        if self.Color   == 'green':
            self.Number = int(random.randint(20,29))
        if self.Color   == 'blue': 
            self.Number = int(random.randint(30,39))
        if self.Color   == 'grey':
            self.Number = int(random.randint(0,39))
        def CheckAnswer(self):
            return (answer)


class Qlist:
    def __init__(self, text):
        self.Questions = [\
        Question("Which escape room is most known? \n\n A. R'dam Escape \n B. Escape010 \n C. Room Escape \n D. Escaperooms", "B"),\
        Question("What tour is not available? \n\n A. Segway \n B. Boat \n C. Car \n D. Bike", "C"),\
        Question("Which of these stores is not located around the Koopgoot? \n\n A. H&M \n B. Media Markt \n C. The Sting \n Six", "B"),\
        Question("For which museum is the monument The Destroyed City made? \n\n A. Harbormuseum \n B. Marinesmuseum \n C. Maritime Museum \n D. Futureland", "C"),\
        Question("At which movie theatre is the Wildlife Film Festival? \n\n A. Cinerama \n B. Pathé de Kuip \n C. Pathé Schouwburgplein \n Euromast", "A"),\
        Question("Where does Rotterdam Tour have its tours? \n\n A. Euromast \n B. Museumplein \n C. Markthal \n D. Central Station", "C"),\
        Question("What country can you also visit in Miniworld Rotterdam? \n\n A. Luxembourg \n B. Germany \n C. France \n D. Spain", "A"),\
        Question("What is the cultural and culinair tour called? \n\n A. Drive & Eat \n B. Bicycle Dine, \n C. Fly for food \n D. Bike & Bite", "D"),\
        Question("Which of the following restaurantboats does not exist? \n\n A. Swanship \n B. Pancakeship \n C. Bearboat \n D. Tapasboat", "A"),\
        Question("Where is the annual autumn carnaval? \n\n A. Stadhuisplein \n B. Pier 80 \n C. Schouwburgplein \n D. Mullerpier", "D"),\
        Question("What is the only building left standing after WW2? \n\n A. Old Harbour \n B. VOC \n C. St Laurenschurch \n D. Euromast", "C"),\
        Question("Who is the Night Mayor? \n\n A. Ahmed Aboutaleb \n B. Jules Deelder \n C. Willem Alexander \n D. Phillipe de Groot", "B"),\
        Question("How did the city get its name? \n\n A. Merchants \n B. Rotte River \n C. the dike \n D. Unknown", "B"),\
        Question("What was Katendrecht known for? \n\n A. Bakers \n B. Prostitutes \n C. old tree \n D. Meat", "B"),\
        Question("When did the zoo open? \n\n A. 2000 \n B. 1975 \n C. 1915 \n D. 1855", "D"),\
        Question("What is the official name of the Koopgoot? \n\n A. Underground shoppingstreet \n B. Beurstraverse \n C. Koopgoot \n D. Harbour", "B"),\
        Question("Which building represents the reconstruction? \n\n A. Bijenkorf \n B. Cube houses \n C. Red Apple \n D. Movie Theater Pathe", "A"),\
        Question("What was the only way to the centre during WW2? \n\n A. Nieuwe binnenweg \n B. Maasbridge \n C. Queensbridge \n D. Erasmusbridge", "B"),\
        Question("Who was the architect that designed the Euromast? \n\n A. Ted Mosby \n B. Brinkman \n C. Koolhaas \n D. Maaskant", "D"),\
        Question("What products did not used to get stored near the harbour? \n\n A. Sugar \n B. Salt \n C. Wool \n D. Cacao", "D"),\
        Question("Which bridge is also called 'The Swan?' \n\n A. Willemsbridge \n B. Erasmusbridge \n C. Briennenoordbrug \n D. Queensbridge", "B"),\
        Question("Which statement is true? \n\n A. Rotterdam is the capital of the Netherlands \n Rotterdam is the capital of South-Holland \n C. Rotterdam is the biggest city of the Netherlands \n D. Rotterdam has the biggest harbour", "D"),\
        Question("Which one is the most important transport? \n\n A. Subway \n B. Car \n C. Bike \n D. Airplane", "A"),\
        Question("How much rain is there on average? \n\n A. 760 to 780mm \n B. 780 to 800mm \n C. 800 to 820mm \n D. 820 to 850mm", "C"),\
        Question("What is the oldest building? \n\n A. Cityhall \n B. St. Laurenschurch \n C. Euromast \n D. Hillegondachurch", "D"),\
        Question("About how many living spaces are there? \n\n A. 150.000 \n B. 300.000 \n C. 450.000, \n 600.000", "C"),\
        Question("How many passengers use public transport daily? \n\n A. 700.000 \n B. 800.000 \n C. 900.000 \n D. 1.000.000", "D"),\
        Question("What is the oldest bridge? \n\n A. Willemsbridge \n B. Queensbridge \n C. Briennenoordbrug \n D. Erasmusbridge", "B"),\
        Question("Another name for the city is? \n\n A. City of miracles \n B. City of cities \n C. City of bridges \n D. Harbour City", "D"),\
        Question("What is Rotterdams biggest river? \n\n A. Maas \n B. Rijn \n C. Waal \n Eiffel", "A"),\
        Question("In what year did the Tour de France kick off in Rotterdam? \n\n A. 2000 \n B. 2005 \n C. 2010 \n D.2015", "C"),\
        Question("What is the yearly tennis event in Ahoy called? \n\n A. ABN AMRO World Tennis \n B. Ahoy Open \n C. Heineken open \n D. Harbor city event", "A"),\
        Question("What is a hockeyclub? \n\n A. HVGR \n B. Focus \n C. HR \n D. HC Rotterdam", "D"),\
        Question("Most populair sport? \n\n A. Fitness \n B. Soccer \n C. Climbing \n D. Basketball", "A"),\
        Question("Who grew up in Rotterdam? \n\n A. Edith Bosch \n B. Denise Maes \n C. Marhinde Verkerk \n D. Dorian van Rijsselberge", "C"),\
        Question("Where did WK rowing take place in 2016? \n\n A. Beatrix Baan \n B. Maasbaan \n C. Juliana Baan \n D. Willem Alexander Baan", "D"),\
        Question("What position did Coun Moulijn play? \n\n A. Right back \n B. Left back \n C. Left winger \n D. Right winger", "C"),\
        Question("What year did the baseball club Neptunes start? \n\n A. 1825 \n B. 1850 \n C. 1875 \n D. 1900", "D"),\
        Question("What is the name of the stadion of soccer club Sparta? \n\n A. The tower \n B. Castle \n C. Kuip \n D. Arena", "B"),\
        Question("How long is the NN marathon? \n\n A. 42,125 km \n B. 42,450 km \n C. 42,680 km \n D. 43,000 km", "A")]          


class Player:
    def __init__(self, color):
        self.at_number = 0
        if color == "red"       : self.Image = pygame.image.load("playerred.png")
        if color == "yellow"    : self.Image = pygame.image.load("playeryellow.png")
        if color == "green"     : self.Image = pygame.image.load("playergreen.png")
        if color == "blue"      : self.Image = pygame.image.load("playerblue.png")

    def SetPosition(self):
        self.at_number  = self.at_number + dice.Number

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
tower               = Tower ()
player              = Player("red")
#player1             = Player("red")
#player2             = Player("yellow")
#player3             = Player("green")
#player4             = Player("blue")
game.Loop()
Terminate()
