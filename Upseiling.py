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
        self.Exit = False
        self.Level = "menu"
            
    def Draw(self, image_destination): 
        self.Load = pygame.image.load(image_destination)
        self.Display.blit(self.Load, (0,0))

    def Update(self): 
        pygame.display.update()
        self.clock.tick(self.FPS)

    def Loop(self): 
        while not self.Exit:
            if self.Level == "menu": 
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.Exit = True 
                self.Draw("background_game_menu.jpg")
                self.Update() # refreshes the window. this is the end of the loop
            #if self.Level == "instructions":
                    #start with video, show empty clickable screen
           #if self.Level == "Instructions":
            #    gameDisplay.blit(bg_emp2, [0, 0])
             #   text("  This game is played with a maximum of 4 players and a minimum of 1. In case it is a single player game, you will be \n  playing against the computer. To start select the number of players and enter their names.  \n \n  Next up is the actual play board. In the clouds in the left corner you will find the name of the player indicating which \n  player�s turn it is, and their score. Next you have the dice, the questions and answering options, and the tower.  \n \n  During the game you can always go back to menu or instructions, the game will be paused and saved. \n \n  The tower indicates how the game is going and who is on a winning streak. The colors represent different categories. \n  Blue is for sports, green is for geography, red is for entertainment, yellow is for history, and grey is random. \n \n  First all players get to roll the dice. This decides who gets the first turn. At the start of a turn the dice has to be thrown \n  again. You will notice your character climbing up the tower to its designated location. The color tells you the category, \n  and you get to see a question with 4 answering options. Press which one you think is correct. The game tells you if the \n  answer is correct or wrong. It will add up in score or the score will stay the same. \n \n  First player to reaches the top, wins!")
              # & 2 buttons
               # if self.Level == "rules":
                #     show rulescreen
                #if self.Level == 'Tutorial' 
                #    show empty screen
                #if self.Level == 'Settings'
                #show empty screen
                #if self.Level == 'highscore'
                #show empty screen
                #if self.Level == 'Winning'
                #show winscreen
                #if self.Level == Game
                #do game
                #
            # you can use elifs here to make new levels
            else: self.Exit = True 

class Button:
    def __init__(self, x, y, w, h, image, constant, pressed, pressing, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.constant = constant
        self.pressed = False
        self.pressing = False
        self.action = action

    def rollover(self):
        if self.x + self.0 > pygame.mouse.get_pos()[0] > self.x and self.y + self.h > pygame.mouse.get_pos()[1] > self.y:
            self.Load = pygame.image.load(image)
            game.Display.blit(self.Load, (0,0))

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

class Dice:
    def __init__(self, x, y, player):
        self.X = x
        self.Y = y
        self.Player = player
        self.Image = image
        self.Number = random.randint(1,6)
    
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
        game.Display.blit(self.Image, [self.X, self.Y])
# ------------------------------------------------------------------ FUNCTIONS ------------------------------------------------------------#

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def text(message):
    def render_textrect(string, font, rect, text_color, background, justification=0):
    
        final_lines = []
        requested_lines = string.splitlines()
        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line 
                    else: 
                        final_lines.append(accumulated_line) 
                        accumulated_line = word + " " 
                final_lines.append(accumulated_line)
            else: 
                final_lines.append(requested_line) 

        surface = pygame.Surface(rect.size) 
        surface.fill(black) 

        accumulated_height = 0 
        for line in final_lines: 
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException 
            accumulated_height += font.size(line)[1]
        return surface
 
    if __name__ == '__main__':
        my_font = pygame.font.SysFont('arial', 20)
        my_string = message 
        my_rect = pygame.draw.rect(gameDisplay, black,[325,105,900,490])
    
        rendered_text = render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 0)

        if rendered_text:
            gameDisplay.blit(rendered_text, my_rect.topleft)

        pygame.display.update()

def terminate():
    pygame.quit()
    quit()

# ------------------------------------------------------------------ RUNNING ------------------------------------------------------------#

game = Game()
startbutton = Button(40, 325, 235, 120, "background_game_menu_button1.png", constant, pressed, pressing, action)
game.Loop()
terminate()
