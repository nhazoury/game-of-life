from config import *


class CellHandler:
    def __init__(self, cells):
        self.cells = cells

    def x_blocks(self):
        return len(self.cells)

    def y_blocks(self):
        if self.x_blocks() == 0:
            return 0
        return len(self.cells[0])

    def is_live(self, x, y):
        return self.cells[y][x]

    def neighbour_is_live(self, x, y, horiz, vert):
        x_ = x + horiz
        y_ = y + vert

        if x_ < 0 or y_ < 0 or x_ >= self.x_blocks() or y_ >= self.y_blocks():
            return False

        return self.is_live(x_, y_)

    def num_live_neighbours(self, x, y):
        count = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.neighbour_is_live(x, y, i, j):
                    count += 1

        if self.is_live(x, y):
            count -= 1

        return count

    def live_in_next(self, x, y):
        return False
