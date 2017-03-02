# Copyright Denise van den Berg - Maes 2017

# Loading modules
import sys, pygame, time, random, os
from pygame.locals import *
from builtins import print
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Screen information
FPS = 60 
fpsClock = pygame.time.Clock()
display_width = 1500
display_height = 750

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Upseiling')
clock = pygame.time.Clock()

# RGB Colours
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)


# Images
bg_menu = pygame.image.load("background_game_menu.jpg")
bg_empty = pygame.image.load("background_empty.jpg")
bg_emp2 = pygame.image.load("background_emp2.jpg")
bg_board = pygame.image.load("background_game_board.jpg")
button1 = pygame.image.load("background_game_menu_button1.png") #start game
button2 = pygame.image.load("background_game_menu_button2.png") #watch tutorial
button3 = pygame.image.load("background_game_menu_button3.png") #settings
button4 = pygame.image.load("background_game_menu_button4.png") #highscores
button5 = pygame.image.load("background_game_menu_button5.png") #instructions
button6 = pygame.image.load("background_game_menu_button6.png") #rules
button7 = pygame.image.load("background_game_menu_button7.png") #quit
button8 = pygame.image.load("background_emp2_button8.png") #quit2
button9 = pygame.image.load("background_emp2_button9.png") #menu
dice1 = pygame.image.load("dice1.png")
dice2 = pygame.image.load("dice2.png")
dice3 = pygame.image.load("dice3.png")
dice4 = pygame.image.load("dice4.png")
dice5 = pygame.image.load("dice5.png")
dice6 = pygame.image.load("dice6.png")
# load audio here

def game_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_menu, [0, 0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        
# add all button actions

        # Button start game
        if 40+235 > mouse[0] > 40 and 325+120 > mouse[1] > 325:
            gameDisplay.blit(button1, [0, 0])
            if click[0] == 1:
                run_game()
        # Button watch tutorial
        if 900+320 > mouse[0] > 980 and 350+120 > mouse[1] > 350:
            gameDisplay.blit(button2, [0, 0])
            if click[0] == 1:
                tutorial()
        # Button settings
        if 1330+150 > mouse[0] > 1330 and 20+60> mouse[1] > 20:
            gameDisplay.blit(button3, [0, 0])
            if click[0] == 1:
                settings_screen()
        # Button highscore
        if 1330+150 > mouse[0] > 1330 and 135+60> mouse[1] > 135:
            gameDisplay.blit(button4, [0, 0])
            if click[0] == 1:
                highscore_screen()
        # Button instructions
        if 7+155 > mouse[0] > 7 and 455+90 > mouse[1] > 455:
            gameDisplay.blit(button5, [0, 0])
            if click[0] == 1:
                instruction_screen()
        # Button rules
        if 170+150 > mouse[0] > 170 and 500+90 > mouse[1] > 500:
            gameDisplay.blit(button6, [0, 0])
            if click[0] == 1:
                rule_screen()
        # Button quit
        if 1380+100 > mouse[0] > 1380 and 590+50 > mouse[1] > 590:
            gameDisplay.blit(button7, [0, 0])
            if click[0] == 1:
                terminate()

        pygame.display.update()
        clock.tick(15)
    
def rule_screen():
    rules = True
    while rules:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_emp2, [0, 0])
        text("The program makes sure cheating is not possible! But there are some rules you need to take into account. \n1. The maximum player amount is 4. \n2. The game only has 1 winner.\n3. For more instructions of the game, watch the tutorial or see instructions on the menu screen.\n\n\nTerms and Conditions \nLast updated: March 01, 2017  \nPlease read these Terms and Conditions carefully before using the Upseiling game. By playing the game you agree to the following terms and conditions:/n This game is made as a project at Rotterdam University of Applied Science and shall not be used in any other way. You are not allowed to sell the game to others or change the code. Manipulation of the game is strictly forbidden. You further acknowledge and agree that Upseiling shall not be responsible or liable, directly or indirectly, for any damage or loss caused or alleged to be caused by downloading or playing the game. Upseiling is copyrighted by Denise van den Berg – Maes, all rights reserved.\n\nThese Terms shall be governed and construed in accordance with the laws of Netherlands, without regard to its conflict of law provisions.")
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if 1380+100 > mouse[0] > 1380 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button8, [0, 0])
            if click[0] == 1:
                terminate()
        if 20+100 > mouse[0] > 20 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button9, [0, 0])
            if click[0] == 1:
                game_menu() 
        pygame.display.update()
        clock.tick(15)

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

def instruction_screen():
    instruct = True
    while instruct:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_emp2, [0, 0])
        
        text("  This game is played with a maximum of 4 players and a minimum of 1. In case it is a single player game, you will be \n  playing against the computer. To start select the number of players and enter their names.  \n \n  Next up is the actual play board. In the clouds in the left corner you will find the name of the player indicating which \n  player’s turn it is, and their score. Next you have the dice, the questions and answering options, and the tower.  \n \n  During the game you can always go back to menu or instructions, the game will be paused and saved. \n \n  The tower indicates how the game is going and who is on a winning streak. The colors represent different categories. \n  Blue is for sports, green is for geography, red is for entertainment, yellow is for history, and grey is random. \n \n  First all players get to roll the dice. This decides who gets the first turn. At the start of a turn the dice has to be thrown \n  again. You will notice your character climbing up the tower to its designated location. The color tells you the category, \n  and you get to see a question with 4 answering options. Press which one you think is correct. The game tells you if the \n  answer is correct or wrong. It will add up in score or the score will stay the same. \n \n  First player to reaches the top, wins!")
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if 1380+100 > mouse[0] > 1380 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button8, [0, 0])
            if click[0] == 1:
                terminate()
        if 20+100 > mouse[0] > 20 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button9, [0, 0])
            if click[0] == 1:
                game_menu() 
        pygame.display.update()
        clock.tick(15)
 
def settings_screen():
    settings = True
    while settings:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_emp2, [0, 0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if 1380+100 > mouse[0] > 1380 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button8, [0, 0])
            if click[0] == 1:
                terminate()
        if 20+100 > mouse[0] > 20 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button9, [0, 0])
            if click[0] == 1:
                game_menu() 
        pygame.display.update()
        clock.tick(15)    
        
def highscore_screen():
    hscore = True
    while hscore:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_emp2, [0, 0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if 1380+100 > mouse[0] > 1380 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button8, [0, 0])
            if click[0] == 1:
                terminate()
        if 20+100 > mouse[0] > 20 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button9, [0, 0])
            if click[0] == 1:
                game_menu() 
        pygame.display.update()
        clock.tick(15)

def tutorial():
    tutorial = True
    while tutorial:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_emp2, [0, 0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if 1380+100 > mouse[0] > 1380 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button8, [0, 0])
            if click[0] == 1:
                terminate()
        if 20+100 > mouse[0] > 20 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button9, [0, 0])
            if click[0] == 1:
                game_menu() 
        pygame.display.update()
        clock.tick(15)

def dice():
    dice = True
    roll=int(random.randint(1,6))
    message_display("You rolled: " +str(roll))
    while dice:
        if roll == 1:
            gameDisplay.blit(dice1, [270, 210])
            break
        if roll == 2:
            gameDisplay.blit(dice2, [270, 210])
            break
        if roll == 3:
            gameDisplay.blit(dice3, [270, 210])
            break
        if roll == 4:
            gameDisplay.blit(dice4, [270, 210])
            break
        if roll == 5:
            gameDisplay.blit(dice5, [270, 210])
            break
        if roll == 6:
            gameDisplay.blit(dice6, [270, 210])
            break
    return roll
    pygame.display.update()
    pygame.time.wait(1000)
    clock.tick(15)

def timer():
    timer = True
    while timer: 
        pygame.draw.rect(gameDisplay, black,(150,450,100,50))
        pygame.display.update()

def run_game():
    run_game = True
    while run_game:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                terminate()
        gameDisplay.blit(bg_board, [0, 0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if 1380+100 > mouse[0] > 1380 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button8, [0, 0])
            if click[0] == 1:
                terminate()
        if 20+100 > mouse[0] > 20 and 670+50 > mouse[1] > 670:
            gameDisplay.blit(button9, [0, 0])
            if click[0] == 1:
                game_menu() 
        if 271+110 > mouse[0] > 271 and 211+110 > mouse[1] > 211:
            if click[0] == 1:
                dice() 
        pygame.display.update()
        clock.tick(15)

def terminate():
    pygame.quit()
    quit()


    """code om locatie te vinden pygame.draw.rect(gameDisplay, red,(1260,725,10,10))""" 

def newposition(player.position, dice(roll)):



class player():
    def __init__ (name, x, y, image, position):
        self.name = name
        self.x = x
        self.y = y
        self.image = image
        self.position = position

    def draw (self):
        gameDisplay.blit(self.image(self.x, self.y))

    def position(self, square):
        square = 0
        if x == 1260 and y == 725:
            square = square + 0
        if x == 1260 and y == 700:
            square = square + 1
        if x == 1260 and y == 680:
            square = square + 2
        if x == 1260 and y == 660:
            square = square + 3
        if x == 1260 and y == 635:
            square = square + 4
        if x == 1260 and y == 605:
            square = square + 5
        if x == 1260 and y == 560:
            square = square + 6
        if x == 1260 and y == 500:
            square = square + 7
        if x == 1260 and y == 450:
            square = square + 8
        if x == 1260 and y == 390:
            square = square + 9
        if x == 1260 and y == 320:
            square = square + 10
        if x == 1260 and y == 220:
            square = square + 11
        if x == 1262 and y == 175:
            square = square + 12
        if x == 1265 and y == 130:
            square = square + 13
        if x == 1270 and y == 100:
            square = square + 14
        if x == 1280 and y == 60:
            square = square + 15
        if x == 1290 and y == 25:
            square = square + 16
        return square

class tower():
    def __init__(self, possquare[]):
        self.possquare = possquare[]

    possquare0 = (1260,725)
    possquare1 = (1260,700)
    possquare2 = (1260,680)
    possquare3 = (1260,660)
    possquare4 = (1260,635)
    possquare5 = (1260,605)
    possquare6 = (1260,560)
    possquare7 = (1260,500)
    possquare8 = (1260,450)
    possquare9 = (1260,390)
    possquare10 = (1260,320)
    possquare11 = (1260,220)
    possquare12 = (1262,175)
    possquare13 = (1265,130)
    possquare14 = (1270,100)
    possquare15 = (1280,60)
    possquare16 = (1290,25)
game_menu()
terminate()