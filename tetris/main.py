import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen_width = 550
screen_height = 800


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

#define colours
bg = (50, 50, 50)
purple = (128,0,128)
cyan = (0, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255,255,0)
orange = (255,165,0)

# Game Vars
tile_size = 50
fps = 60

# Images
cursor_img = pygame.image.load("images/cursor.png")

# Grid
def draw_grid():
    for line in range(0, 16):
        pygame.draw.line(screen, (200, 200, 200), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (200, 200, 200), (line * tile_size, 0), (line * tile_size, screen_height))


# Agreeeable Positions
x = 0
y = 0

x_p = []
y_p = []

while x <= screen_width:
    x_p.append(x)
    x += 25
while y <= screen_height:
    y_p.append(y)
    y += 25

c = 0
e = 0

good_pos = []
while c <= len(x_p)-1:
    while e <= len(y_p)-1:
        a = (x_p[c], y_p[e])
        good_pos.append(a)
        e += 1
    c += 1
    e = 0



class Cursor():
    def __init__(self, x, y):
        self.image = cursor_img.get_rect()

run = True
while run:

    clock.tick(fps)


    position = pygame.mouse.get_pos()


    # Blocks
    def purple_block():
        pygame.draw.rect(screen, purple, (position[0], position[1], tile_size, tile_size))
        pygame.draw.rect(screen, purple, (position[0]+tile_size, position[1], tile_size, tile_size))
        pygame.draw.rect(screen, purple, (position[0]-tile_size, position[1], tile_size, tile_size))
        pygame.draw.rect(screen, purple, (position[0], position[1]+tile_size, tile_size, tile_size))

    screen.fill(bg)
    if rect.collidepoint(x, y) in good_pos:
        purple_block()
    draw_grid()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
