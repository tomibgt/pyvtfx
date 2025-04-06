import sys, time

sys.path.append('/Users/bgt/gitty/pyvtfx/src')

import pyvtfx

def test_foundations():
    x, y = pyvtfx.get_cursor_position()
    assert x is not None
    assert y is not None
    assert x >0
    assert y > 0

