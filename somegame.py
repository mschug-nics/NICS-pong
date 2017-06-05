import pygame
# Global Constants
screen_width = 640
screen_height = 480
# Initialization
pygame.init()
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

while running:
        clock.tick(300)
        screen.fill((200, 200, 200))
        screen.blit(player1,player1pos)
        screen.blit(player2,player2pos)
        screen.blit(ball,ballpos)
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
