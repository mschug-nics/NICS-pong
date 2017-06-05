import pygame
screen_width = 640
screen_height = 480
pygame.init()
pygame.display.set_caption("Ping!")
screen = pygame.display.set_mode((screen_width, screen_height))
player1pos = pygame.Rect(0,screen_height/2-24,16,48)
player2pos = pygame.Rect(screen_width-16,screen_height/2-24,16,48)
ballpos = pygame.Rect(screen_width/2+8,screen_height/2+8,16,16)
player1 = pygame.image.load("player1.png")
player2 = pygame.image.load("player2.png")
ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()
running=True
while running:
        clock.tick(300)
        screen.fill((66, 164, 244))
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
