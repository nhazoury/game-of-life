import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BLOCK_LENGTH = 20

BLOCKS_X = 20
BLOCKS_Y = 20

BORDER_THICKNESS = 1

WINDOW_WIDTH = ((2 * BORDER_THICKNESS) + BLOCK_LENGTH) * BLOCKS_X
WINDOW_HEIGHT = ((2 * BORDER_THICKNESS) + BLOCK_LENGTH) * BLOCKS_Y


def main():
    global SCREEN
    pygame.init()
    pygame.display.set_caption('Conway\'s Game of Life by nhazoury')
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCK_LENGTH + 2 * BORDER_THICKNESS):
        for y in range(0, WINDOW_HEIGHT, BLOCK_LENGTH + 2 * BORDER_THICKNESS):
            rect = pygame.Rect(x + BORDER_THICKNESS, y + BORDER_THICKNESS, BLOCK_LENGTH, BLOCK_LENGTH)
            pygame.draw.rect(SCREEN, WHITE, rect, 0)


if __name__ == "__main__":
    main()
