import pygame
import random
from datetime import datetime
# Global Constants
screen_width = 640
screen_height = 480
balldx = -1
balldy = -1
player1_score = 0
player2_score = 0
# Initialization
pygame.init()
random.seed(datetime.now())
pygame.font.init()
myfont = pygame.font.Font("wts11.ttf",64)
pygame.display.set_caption("Ping!")
screen = pygame.display.set_mode((screen_width, screen_height))
player1pos = pygame.Rect(0,screen_height/2-24,16,48)
player2pos = pygame.Rect(screen_width-16,screen_height/2-24,16,48)
ballpos = pygame.Rect(screen_width/2-8,screen_height/2-8,16,16)
player1 = pygame.image.load("player1.png")
player2 = pygame.image.load("player2.png")
ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()
running=True

# Assume each player is 16x48
def move_player(person,dy):
        person.y = person.y + dy
        # This is where we check for walls
        if person.y > screen_height-48:
                # Move Down
                person.y=screen_height-48
        if person.y < 0:
                # Move Up
                person.y=0
                
# Assume ball is 16x16
def move_ball():
        global balldx
        global balldy
        global player1_score
        global player2_score
        ballpos.x = ballpos.x + balldx
        ballpos.y = ballpos.y + balldy
        # Check for collision with bounds

        if ballpos.x < 0:
                # score a point for player 2
                player2_score=player2_score+1
                # reset ball position
                ballpos.x = screen_width/2-8
                ballpos.y = screen_height/2-8
        if ballpos.x > screen_width-16:
                # score a point for player 1
                player1_score=player1_score+1
                # reset the ball position
                ballpos.x = screen_width/2-8
                ballpos.y = screen_height/2-8
        if ballpos.y < 0:
                # bounce by reversing dy
                balldy = -balldy
                #print("Reversing balldy. Now "+str(balldy))
                #ballpos.y = ballpos.y + balldy
        if ballpos.y > screen_height-16:
                # bounce by reversing dy
                balldy = -balldy
                #print("Reversing balldy. Now "+str(balldy))
                #ballpos.y = ballpos.y + balldy
        # Check for collision with players
        if ballpos.colliderect(player1pos):
                balldx = -balldx
        if ballpos.colliderect(player2pos):
                balldx = -balldx

while running:
        clock.tick(300)
        screen.fill((200, 200, 200))
        screen.blit(player1,player1pos)
        screen.blit(player2,player2pos)
        screen.blit(ball,ballpos)
        screen.blit(myfont.render(str(player1_score),True,(255,255,255)),(70,0))
        screen.blit(myfont.render(str(player2_score),True,(255,255,255)),(screen_width-50-70,0))
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.QUIT:
                        pygame.quit()
                        running=False
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
                pygame.quit()
                running=False
        if key[pygame.K_a]:
                # Player 1 Up
                move_player(player1pos,-1)
        if key[pygame.K_z]:
                # Player 1 Down
                move_player(player1pos,1)
        if key[pygame.K_k]:
                # Player 2 Up
                move_player(player2pos,-1)
        if key[pygame.K_m]:
                # Player 2 Down
                move_player(player2pos,1)
        move_ball()
