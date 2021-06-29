import os
from typing import Any

import pygame

from .objects import Shape
from .settings import (BASE_DIR, BLOCK_SIZE, PLAY_HEIGHT, PLAY_WIDTH,
                       TOP_LEFT_X, TOP_LEFT_Y)

SCORES = os.path.join(BASE_DIR, 'scores.txt')


def create_grid(locked_pos={}) -> list[list[tuple[int, int, int]]]:
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                grid[i][j] = locked_pos[(j, i)]
    return grid


def convert_shape_format(shape: Shape) -> list:
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape: Shape, grid: list[list[tuple[int, int, int]]]) -> bool:
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)]
                    for i in range(20)]
    accepted = [j for sub in accepted_pos for j in sub]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions: Any) -> bool:
    for pos in positions:
        _, y = pos
        if y < 1:
            return True
    return False


def get_shape() -> Shape:
    return Shape(5, 0)


def draw_text_middle(surface: Any, text, size: int, color: tuple[int, int,
                                                                 int]) -> None:
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, True, color)

    surface.blit(label,
                 (TOP_LEFT_X + PLAY_WIDTH / 2 - (label.get_width() / 2),
                  TOP_LEFT_Y + PLAY_HEIGHT / 2 - label.get_height() / 2))


def draw_grid(surface: Any, grid: list[list[tuple[int, int, int]]]):
    sx = TOP_LEFT_X
    sy = TOP_LEFT_Y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * BLOCK_SIZE),
                         (sx + PLAY_WIDTH, sy + i * BLOCK_SIZE))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128),
                             (sx + j * BLOCK_SIZE, sy),
                             (sx + j * BLOCK_SIZE, sy + PLAY_HEIGHT))


def clear_rows(grid: list[list[tuple[int, int, int]]], locked: dict) -> int:
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc


def draw_next_shape(shape: Shape, surface: Any) -> None:
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Style', True, (255, 255, 255))

    sx = TOP_LEFT_X + PLAY_WIDTH + 50
    sy = TOP_LEFT_Y + PLAY_HEIGHT / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color,
                                 (sx + j * BLOCK_SIZE, sy + i * BLOCK_SIZE,
                                  BLOCK_SIZE, BLOCK_SIZE), 0)

    surface.blit(label, (sx + 10, sy - 30))


def update_score(current_score: int) -> None:
    highest = high_score()
    with open(SCORES, 'a+') as f:
        if current_score > int(highest):
            f.seek(0)
            f.truncate(0)
            f.write(str(current_score))


def high_score() -> str:
    with open(SCORES, 'a+') as f:
        f.seek(0)
        score = f.read()
        if score.isdigit():
            return score
    return '0'


def draw_window(surface: Any,
                grid: list[list[tuple[int, int, int]]],
                score: int = 0,
                last_score: str = '0') -> None:
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', True, (255, 255, 255))

    surface.blit(label,
                 (TOP_LEFT_X + PLAY_WIDTH / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), True, (255, 255, 255))

    sx = TOP_LEFT_X + PLAY_WIDTH + 50
    sy = TOP_LEFT_Y + PLAY_HEIGHT / 2 - 100

    surface.blit(label, (sx + 20, sy + 160))
    # last score
    label = font.render('High Score: ' + last_score, True, (255, 255, 255))

    sx = TOP_LEFT_X - 200
    sy = TOP_LEFT_Y + 200

    surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (TOP_LEFT_X + j * BLOCK_SIZE, TOP_LEFT_Y +
                              i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    pygame.draw.rect(surface, (255, 0, 0),
                     (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 5)

    draw_grid(surface, grid)
