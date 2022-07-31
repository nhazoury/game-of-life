class CellHandler:
    def __init__(self, cells):
        self.cells = cells

    def is_live(self, x, y):
        return self.cells[y][x]
