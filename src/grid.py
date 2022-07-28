import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLOCK_LENGTH = 20

BLOCKS_X = 40
BLOCKS_Y = 40

BORDER_THICKNESS = 1

WINDOW_WIDTH = (BORDER_THICKNESS + BLOCK_LENGTH) * BLOCKS_X + BORDER_THICKNESS
WINDOW_HEIGHT = (BORDER_THICKNESS + BLOCK_LENGTH) * BLOCKS_Y + BORDER_THICKNESS


def main():
    global SCREEN
    pygame.init()
    pygame.display.set_caption('Conway\'s Game of Life by nhazoury')
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)

    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_LENGTH + BORDER_THICKNESS):
        for y in range(0, WINDOW_HEIGHT, BLOCK_LENGTH + BORDER_THICKNESS):
            rect = pygame.Rect(x + BORDER_THICKNESS, y + BORDER_THICKNESS, BLOCK_LENGTH, BLOCK_LENGTH)
            pygame.draw.rect(SCREEN, WHITE, rect, 0)


def calc_true_coord(n):
    return (BORDER_THICKNESS + BLOCK_LENGTH) * n


def draw_cell(x, y, colour):
    x_ = calc_true_coord(x)
    y_ = calc_true_coord(y)

    rect = pygame.Rect(x_ + BORDER_THICKNESS, y_ + BORDER_THICKNESS, BLOCK_LENGTH, BLOCK_LENGTH)
    pygame.draw.rect(SCREEN, colour, rect, 0)


if __name__ == "__main__":
    main()
