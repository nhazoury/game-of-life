class CellHandler:
    def __init__(self, cells):
        self.cells = cells

    def is_live(self, x, y):
        return self.cells[y][x]

    def num_live_neighbours(self, x, y):
        return 0
