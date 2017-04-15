# Copyright Denise van den Berg - Maes 2017

# Loading modules
import pygame, random, os, psycopg2
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#----------------------------------------------------------  LOCALS ---------------------------------------------------

# RGB Colours
Black           = (0,       0,      0)
White           = (255,     255,    255)

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
        self.Turn       = "player1"
        self.Music      = True
        self.Sounds     = True
        self.Images     = [\
                        pygame.image.load("background_game_menu.jpg"),\
                        pygame.image.load("background_empty.jpg"),\
                        pygame.image.load("background_emp2.jpg"),\
                        pygame.image.load("background_game_board.jpg"),\
                        pygame.image.load("background_winscreen.jpg"),\
                        pygame.image.load("background_emp2_instr.jpg"),\
                        pygame.image.load("background_emp2_rules.jpg"),\
                        pygame.image.load("background_emp2_settings.png")]
            
    def Draw(self, image_number): 
        self.Display.blit(self.Images[image_number], (0,0))

    def Update(self): 
        pygame.display.update()
        self.Clock.tick(self.FPS)

    def Loop(self): 
        music.PlayingMusic()
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
                self.Draw(7)
                quitbutton2.Draw()
                menubutton.Draw()
                settingsbutton3.Draw()
                settingsbutton2.Draw()
                settingsbutton1.Draw()
                settingsbutton0.Draw()
                soundsbutton1.Draw()
                soundsbutton0.Draw()
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
                if self.Turn == "player 1":
                    text('Turn: Player 1', 150, (game.Width/4),(game.Height/3), Black)
                if self.Turn == "player 2":
                    text('Turn: Player 1', 150, (game.Width/4),(game.Height/3), Black)
                player2.Draw()                
                player1.Draw()
                dice.Draw()
                question.Draw()
                self.Update()    
            elif self.Level == "winning": 
                pygame.mixer.music.stop()
                music.Effects('applause')
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Terminate = True 
                self.Draw(4)
                quitbutton2.Draw()
                menubutton.Draw()
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
        self.Number     = 0
        self.Pressed    = False
        self.Clickable  = True
        self.FakePressed = False
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
        if game.Turn == "player1":
            if self.Clickable == True:
                if self.X + self.W > pygame.mouse.get_pos()[0] > self.X and self.Y + self.H >  pygame.mouse.get_pos()[1] > self.Y:
                    game.Display.blit(self.Images [0], (self.X, self.Y))
                    if pygame.mouse.get_pressed()[0] == True:
                        self.Roll()
                        self.Pressed = True
                    elif self.Pressed == True:
                        question.SetQuestion()
                        self.Pressed = False
                        self.Clickable = False
        if game.Turn == "player2": #werkt niet, miss in roll?
            times = 0  
            for times in range(1):
                times = times + 1  
                if times <= 1:           
                    self.Roll()
                    break
                elif times >= 1:
                    question.SetQuestion()
                break

    def Roll(self):
        self.Number = int(random.randint(1,6))
        return (self.Number)

class Square:
    def __init__(self, color, posx, posy):
        self.Color  = color
        self.X      = posx
        self.Y      = posy

    def GetPosition(self):
        if tower.Squares[player1.at_number <= 16] :
            return [self.X, self.Y]
        else:
            winning()
        if tower.Squares[player2.at_number <= 16] :
            return [self.X, self.Y]
        else:
            winning()

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
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 ),\
            Square("win",     1290, 25 )]

class Question:
    def __init__(self, x, y):
        self.X            = x
        self.Y            = y
        self.Number       = 0
        self.QuestionTime = False
        self.Answer       = ""
        self.Buttons      = [\
                            Button(431,   610,     57,    113,    "Overlay_A.png",    self.QA),\
                            Button(555,   605,     61,    110,    "Overlay_B.png",    self.QB),\
                            Button(674,   603,     65,    112,    "Overlay_C.png",    self.QC),\
                            Button(806,   609,     57,    119,    "Overlay_D.png",    self.QD)]
        self.Images       = [\
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
                        pygame.image.load("QB10.png"),\
                        pygame.image.load("correct.png"),\
                        pygame.image.load("incorrect.png")]

    def Draw(self):
        if self.QuestionTime == True:
            game.Display.blit(self.Images[self.Number], (self.X, self.Y))
            for button in self.Buttons:
                button.Draw()
            
    def SetQuestion(self):
        if game.Turn == "player1":
            color = tower.Squares[player1.at_number + dice.Number].Color
        elif game.Turn == "player2":
            color = tower.Squares[player2.at_number + dice.Number].Color
        if      color == "red":     self.Number = random.randint(0,9)
        elif    color == "yellow":  self.Number = random.randint(10,19)
        elif    color == "green":   self.Number = random.randint(20,29)
        elif    color == "blue":    self.Number = random.randint(30,39)
        elif    color == "grey":    self.Number = random.randint(0,39)
        self.QuestionTime = True

    def setCorrect(self, number, choice):
        self.Number = number
        self.Answer = choice
        if   self.Number == 0  and self.Answer == "B": self.Correct = True
        elif self.Number == 1  and self.Answer == "C": self.Correct = True
        elif self.Number == 2  and self.Answer == "B": self.Correct = True
        elif self.Number == 3  and self.Answer == "C": self.Correct = True
        elif self.Number == 4  and self.Answer == "A": self.Correct = True
        elif self.Number == 5  and self.Answer == "C": self.Correct = True
        elif self.Number == 6  and self.Answer == "A": self.Correct = True
        elif self.Number == 7  and self.Answer == "D": self.Correct = True
        elif self.Number == 8  and self.Answer == "A": self.Correct = True
        elif self.Number == 9  and self.Answer == "D": self.Correct = True
        elif self.Number == 10 and self.Answer == "C": self.Correct = True
        elif self.Number == 11 and self.Answer == "B": self.Correct = True
        elif self.Number == 12 and self.Answer == "B": self.Correct = True
        elif self.Number == 13 and self.Answer == "B": self.Correct = True
        elif self.Number == 14 and self.Answer == "D": self.Correct = True
        elif self.Number == 15 and self.Answer == "B": self.Correct = True
        elif self.Number == 16 and self.Answer == "A": self.Correct = True
        elif self.Number == 17 and self.Answer == "B": self.Correct = True
        elif self.Number == 18 and self.Answer == "D": self.Correct = True
        elif self.Number == 19 and self.Answer == "D": self.Correct = True
        elif self.Number == 20 and self.Answer == "B": self.Correct = True
        elif self.Number == 21 and self.Answer == "D": self.Correct = True
        elif self.Number == 22 and self.Answer == "A": self.Correct = True
        elif self.Number == 23 and self.Answer == "C": self.Correct = True
        elif self.Number == 24 and self.Answer == "D": self.Correct = True
        elif self.Number == 25 and self.Answer == "C": self.Correct = True
        elif self.Number == 26 and self.Answer == "D": self.Correct = True
        elif self.Number == 27 and self.Answer == "B": self.Correct = True
        elif self.Number == 28 and self.Answer == "D": self.Correct = True
        elif self.Number == 29 and self.Answer == "A": self.Correct = True
        elif self.Number == 30 and self.Answer == "C": self.Correct = True
        elif self.Number == 31 and self.Answer == "A": self.Correct = True
        elif self.Number == 32 and self.Answer == "D": self.Correct = True
        elif self.Number == 33 and self.Answer == "A": self.Correct = True
        elif self.Number == 34 and self.Answer == "C": self.Correct = True
        elif self.Number == 35 and self.Answer == "D": self.Correct = True
        elif self.Number == 36 and self.Answer == "C": self.Correct = True
        elif self.Number == 37 and self.Answer == "D": self.Correct = True
        elif self.Number == 38 and self.Answer == "B": self.Correct = True
        elif self.Number == 39 and self.Answer == "A": self.Correct = True
        else: self.Correct = False

    def GetAnswer(self):
        '''if game.Turn == "player2":
            choices = ["A", "B", "C", "D"] #dit klopt nog niet 
            dice.Roll()
            self.SetQuestion()
            self.setCorrect(dice.Number, random.choice(choices))'''
        if game.Turn == "player1":
            self.setCorrect(self.Number, self.Answer)
        if self.Correct == True and game.Turn == "player1": 
            player1.SetPosition() 
            player1.score += 1
            self.CorrectA()
        elif self.Correct == False and game.Turn == "player1":
            self.InCorrectA()
            player1.score -=1
        if self.Correct == True and game.Turn == "player2": 
            player2.score += 1
            player2.SetPosition() 
            self.CorrectA()
        elif self.Correct == False:
            self.InCorrectA()
            player2.score -=1
        TurnOver()
        self.QuestionTime = False

    def CorrectA(self):
        checking = True
        while checking == True:
            game.Display.blit(self.Images[40], (0, 0))
            music.Effects('correct')
            game.Update()
            pygame.time.wait(1000)
            checking = False

    def InCorrectA(self):
        checking = True
        while checking == True:
            game.Display.blit(self.Images[41], (0, 0))
            music.Effects('incorrect')
            game.Update()
            pygame.time.wait(1000)
            checking = False

    def QA(self):
        question.Answer = "A"
        question.GetAnswer()

    def QB(self):
        question.Answer = "B"
        question.GetAnswer()

    def QC(self):
        question.Answer = "C"
        question.GetAnswer()

    def QD(self):
        question.Answer = "D"
        question.GetAnswer()

class Player:
    def __init__(self, color, score, player):
        self.at_number = 0
        self.score = 0
        self.player = player
        if player == "player1":
            if color == "red":       
                self.Image = pygame.image.load("playerred.png")
        elif player == "player2":
            if color == "yellow":    
                self.Image = pygame.image.load("playeryellow.png")

    def SetPosition(self):
        self.at_number  = self.at_number + 1
        if self.at_number >= 16:
            winning()
        print(self.at_number)

    def Draw(self): 
        game.Display. blit(self.Image, tower.Squares[self.at_number].GetPosition())
        print ("positie ", self.player, ": ", self.at_number)


class Music:
    def __init__(self):
        self.CorrectEffect   = pygame.mixer.Sound('right.wav')
        self.InCorrectEffect = pygame.mixer.Sound('wrong.wav')
        self.pling           = pygame.mixer.Sound('danzon.wav')
        self.applause        = pygame.mixer.Sound('applause.wav')
        self.Music           = pygame.mixer.music.load('happybeesurf.wav')  
        
    def Effects(self, kindofsound):
        if game.Sounds == True:
            if kindofsound == 'correct':
                self.CorrectEffect.play()
            elif kindofsound == 'incorrect':
                self.InCorrectEffect.play()
            elif kindofsound == 'applause':
                self.applause.play()
            elif kindofsound == 'pling':
                self.pling.play()

    def PlayingMusic(self):
        if game.Music == True:
            pygame.mixer.music.play(-1)
        elif game.Music == False:
            pygame.mixer.music.stop()

    def SoundsVolume3(self):
        game.Sounds = True
        music.Effects('pling')
        text('Sound Effects: On', 150, (game.Width/4),(game.Height/3), White)
        game.Update()
        pygame.time.wait(750)
    def SoundsVolume0(self):
        game.Sounds = False
        text('Sound Effects: Off', 150, (game.Width/4),(game.Height/3), White)
        game.Update()
        pygame.time.wait(750)

    def MusicVolume3(self):
        game.Music = True
        pygame.mixer.music.set_volume(1.0)
        self.PlayingMusic()
        text('Music Volume : 3', 150, (game.Width/4),(game.Height/3), White)
        game.Update()
        pygame.time.wait(750)
    def MusicVolume2(self):
        game.Music = True
        pygame.mixer.music.set_volume(0.65)
        self.PlayingMusic()
        text('Music Volume : 2', 150, (game.Width/4),(game.Height/3), White)
        game.Update()
        pygame.time.wait(750)
    def MusicVolume1(self):
        game.Music = True
        pygame.mixer.music.set_volume(0.35)
        self.PlayingMusic()
        text('Music Volume : 1', 150, (game.Width/4),(game.Height/3), White)
        game.Update()
        pygame.time.wait(750)
    def MusicVolume0(self):
        game.Music = False
        self.PlayingMusic()
        text('Music Volume : OFF', 150, (game.Width/4),(game.Height/3), White)
        game.Update()
        pygame.time.wait(750)
# ------------------------------------------------------------------ FUNCTIONS ------------------------------------------------------------#

def text(text, size, x, y, textcolor):
    font = pygame.font.SysFont(None, size)
    blittext = font.render(text, True, textcolor)
    game.Display.blit(blittext, [x,y])

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

def winning():
    game.Level ="winning"

def TurnOver():
    if game.Turn == "player1":
        text('Turn: Player 2', 150, (game.Width/4),(game.Height/3), Black)
        game.Update()
        pygame.time.wait(1500)
        game.Turn = "player2"
        dice.Clickable = False
    elif game.Turn == "player2":
        text('Turn: Player 1', 150, (game.Width/4),(game.Height/3), Black)
        game.Update()
        pygame.time.wait(1500)
        game.Turn = "player1"
        dice.Clickable = True

def Terminate():
    pygame.quit()
    quit()

# ------------------------------------------------------------------ RUNNING ------------------------------------------------------------#

game                = Game()
music               = Music()
startbutton         = Button(40,    325,    235,    120,    "background_game_menu_button1.png", startgame) 
tutorialbutton      = Button(900,   350,    320,    120,    "background_game_menu_button2.png", starttutorial) 
settingsbutton      = Button(1330,   20,    150,     60,    "background_game_menu_button3.png", startsettings) 
highscoresbutton    = Button(1330,  135,    150,     60,    "background_game_menu_button4.png", starthighscores) 
instructionsbutton  = Button(7,     455,    155,     90,    "background_game_menu_button5.png", startinstructions) 
rulesbutton         = Button(170,   500,    150,     90,    "background_game_menu_button6.png", startrules) 
quitbutton          = Button(1380,  590,    100,     50,    "background_game_menu_button7.png", Terminate) 
quitbutton2         = Button(1380,  670,    100,     50,    "background_emp2_button8.png",      Terminate) 
menubutton          = Button(20,    670,    100,     50,    "background_emp2_button9.png",      startmenu) 
settingsbutton3     = Button(494,   437,     33,    161,    "settingsbuttonmusic3.png",         music.MusicVolume3)
settingsbutton2     = Button(445,   458,     30,     95,    "settingsbuttonmusic2.png",         music.MusicVolume2)
settingsbutton1     = Button(416,   476,     38,     75,    "settingsbuttonmusic1.png",         music.MusicVolume1)
settingsbutton0     = Button(288,   425,    120,    180,    "settingsbuttonmusic0.png",         music.MusicVolume0)
soundsbutton1       = Button(1000,  405,    115,    205,    "soundsbutton1.png",                music.SoundsVolume3)
soundsbutton0       = Button(1130,  428,    115,    175,    "soundsbutton0.png",                music.SoundsVolume0)
dice                = Dice  (270,   210,    116,    116)
question            = Question(470, 80)
tower               = Tower ()
player1             = Player("red", 0, "player1")
player2             = Player("yellow", 0, "player2")
game.Loop()
Terminate()