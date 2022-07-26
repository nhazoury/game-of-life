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
        return self.cells[x][y]

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
        n = self.num_live_neighbours(x, y)
        if self.is_live(x, y):
            if n == 2 or n == 3:
                return True
        else:
            if n == 3:
                return True

        return False

    def next_interation(self):
        new = [[False for j in range(self.y_blocks())] for i in range(self.x_blocks())]
        for x in range(self.x_blocks()):
            for y in range(self.y_blocks()):
                new[x][y] = self.live_in_next(x, y)
        self.cells = new

    def set_live(self, x, y):
        self.cells[x][y] = True

    def set_dead(self, x, y):
        self.cells[x][y] = False
