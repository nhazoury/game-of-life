import sys

import pygame

from config import *
from patterns import *

cells = [[False for j in range(BLOCKS_Y)] for i in range(BLOCKS_X)]
cellHandler = CellHandler(cells)
patternMaker = PatternMaker(cellHandler)


def main():
    global SCREEN
    pygame.init()
    pygame.display.set_caption('Conway\'s Game of Life by nhazoury')
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)
    CLOCK = pygame.time.Clock()

    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        cellHandler.next_interation()
        CLOCK.tick(FPS)


def draw_grid():
    for x in range(0, BLOCKS_X):
        for y in range(0, BLOCKS_Y):
            draw_cell(x, y, get_colour(x, y))


def draw_cell(x, y, colour):
    x_ = calc_true_coord(x)
    y_ = calc_true_coord(y)

    rect = pygame.Rect(x_, y_, BLOCK_LENGTH, BLOCK_LENGTH)
    pygame.draw.rect(SCREEN, colour, rect, 0)


def get_colour(x, y):
    if cellHandler.is_live(x, y):
        return LIVE
    return DEAD


def calc_true_coord(n):
    return (BORDER_THICKNESS + BLOCK_LENGTH) * n + BORDER_THICKNESS
