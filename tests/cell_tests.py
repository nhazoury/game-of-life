from src.cell import is_live

testCells = [[True,  True,  False, True ],
             [False, False, False, False],
             [False, False, True,  False],
             [False, True,  False, False]]

def test_checks_live_status():
    assert is_live(3, 0)

def test_checks_dead_status():
    assert not is_live(0, 2)