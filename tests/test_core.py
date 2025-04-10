import sys, termios

sys.path.append('/Users/bgt/gitty/pyvtfx/src')

import pyvtfx

def test_foundations():
    x, y = pyvtfx.get_cursor_position()
    assert x is not None
    assert y is not None
    assert x > 0
    assert y > 0

def test_set_cursor_position():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save terminal settings

    pyvtfx.set_cursor_position(7, 7)
    x, y = pyvtfx.get_cursor_position()

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings

    assert x == 7 and y == 7
