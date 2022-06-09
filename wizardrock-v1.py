import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

rock_width = 50
rock_height = 50

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("wizard rock!!")
clock = pygame.time.Clock()

rockImg = pygame.image.load('./Documents/coding/wizardrock/myrock.png')
rockImg = pygame.transform.scale(rockImg, (50,50))

def rock(x,y):
    gameDisplay.blit(rockImg, (x,y))

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.45)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                elif event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        rock(x,y)

 

        if x < 0 : x = 0
        if x > display_width - rock_width : x = display_width - rock_width
        if y < 0 : y = 0
        if y > display_height - rock_height : y = display_height - rock_height

            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
