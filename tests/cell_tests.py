from cell import CellHandler

testCells = [[True, True, True, True],
             [False, True, False, False],
             [False, False, True, False],
             [False, True, False, False]]

c = CellHandler(testCells)


def test_checks_live_status():
    assert c.is_live(3, 0)


def test_checks_dead_status():
    assert not c.is_live(0, 2)


def test_number_of_live_neighbours_of_dead_cell():
    assert c.num_live_neighbours(1, 1) == 4


def test_number_of_live_neighbours_of_live_cell():
    assert c.num_live_neighbours(2, 2) == 2

def test_number_of_live_neighbours_of_border_cell():
    assert c.num_live_neighbours(0, 3) == 1
