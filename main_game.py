import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

game_Display = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('The Dead King')

pygame.display.update()

game_Exit = False

while not game_Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Exit = True

    game_Display.fill(white, rect=[10,300,980,190])
    pygame.display.update()

pygame.quit()
quit()
