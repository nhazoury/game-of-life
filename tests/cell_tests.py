from cell import CellHandler

testCells = [[True,  True,  False, True ],
             [False, False, False, False],
             [False, False, True,  False],
             [False, True,  False, False]]

c = CellHandler(testCells)
def test_checks_live_status():
    assert c.is_live(3, 0)

def test_checks_dead_status():
    assert not c.is_live(0, 2)