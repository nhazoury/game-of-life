from cell import CellHandler


class PatternMaker:
    def __init__(self, c: CellHandler):
        self.c = c



    def blinker(self, x, y):
        self.c.set_live(x, y)
        self.c.set_live(x + 1, y)
        self.c.set_live(x + 2, y)


    def glider(self, x, y):
        self.blinker(x, y)
        self.c.set_live(x, y + 1)
        self.c.set_live(x + 1, y + 2)


    def f_pentomino(self, x, y):
        self.c.set_live(x + 1, y)
        self.c.set_live(x + 2, y)
        self.c.set_live(x, y + 1)
        self.c.set_live(x + 1, y + 1)
        self.c.set_live(x + 1, y + 2)
