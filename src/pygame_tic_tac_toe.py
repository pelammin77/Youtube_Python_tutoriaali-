import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600

RED = (255, 0, 0)
GREEN =(0, 0, 255)
LINE_COLOR = (138, 122, 102)
BACGROUD_COLOR =(219, 189, 143)
LINE_TICKNESS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT) )
pygame.display.set_caption("Jatkanshakki")
screen.fill(BACGROUD_COLOR)

def draw_board():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200),LINE_TICKNESS )
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400),LINE_TICKNESS )

    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_TICKNESS)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_TICKNESS)


draw_board()
while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

