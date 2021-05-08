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

# Grid
def draw_grid():
    for line in range(0, 16):
        pygame.draw.line(screen, (200, 200, 200), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (200, 200, 200), (line * tile_size, 0), (line * tile_size, screen_height))


data = 100
'''
# World 
row_count = 0
for row in data:
    col_count = 0
    for tile in row:
        col_count += 1
    row_count += 1
'''



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
    purple_block()
    draw_grid()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
