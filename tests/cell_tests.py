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


def test_live_in_next_case_1():
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    assert not c.live_in_next(3, 0)


def test_live_in_next_case_2():
    # Any live cell with two or three live neighbours lives on to the next generation.
    assert c.live_in_next(1, 0)


def test_live_in_next_case_3():
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    assert not c.live_in_next(1, 1)


def test_live_in_next_case_4():
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    assert c.live_in_next(1, 2)
