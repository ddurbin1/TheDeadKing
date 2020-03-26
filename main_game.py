import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

width = 1000
height = 500

game_Display = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Dead King')

font = pygame.font.SysFont(None, 30)


def message_to_screen(msg,color,space):
    screen_text = font.render(msg, True, color)
    game_Display.blit(screen_text, [10, 10+(30*space)])
    pygame.display.update()

game_Exit = False

while not game_Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Exit = True

    game_Display.fill(white, rect=[10,300,980,190])
    message_to_screen("Welcome to the beta of 'The Dead King', It's a work in progress so don't be surprised if it's bad.", red, 0)
    pygame.display.update()
    


pygame.quit()
quit()
