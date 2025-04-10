from colorama import init
import sys
import tty
import termios

def clear_screen():
    sys.stdout.write("\033[2J")
    sys.stdout.flush()


def get_console_size() -> list[int, int]:
    """Retrieve console size using ANSI escape codes."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save terminal settings
    try:
        tty.setcbreak(fd)  # Set terminal to raw mode

        # Store curson position
        row, col = get_cursor_position()

        # Move cursor to bottom-right
        set_cursor_position(999, 999)

        # Ask for cursor position
        rows, cols = get_cursor_position()

        # Move cursor back
        set_cursor_position(row, col)

        return [rows, cols]

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings

def get_cursor_position() -> list[int, int]:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save terminal settings
    try:
        # Disable canonical mode and echo
        new_settings = termios.tcgetattr(fd)
        new_settings[3] = new_settings[3] & ~termios.ICANON & ~termios.ECHO  # Disable canonical mode and echo
        termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)

        # Ask for cursor position
        sys.stdout.write("\033[6n")
        sys.stdout.flush()

        # Read response: should be `\033[y;xR`
        response = ""
        while True:
            ch = sys.stdin.read(1)
            response += ch
            if ch == "R":  # End of sequence
                break

        # Parse response: "\033[y;xR"
        rows, cols = map(int, response[2:-1].split(";"))
        return [rows, cols]

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings

def set_color(color: int):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save terminal settings
    try:
        sys.stdout.write(f"\033[1;{color}m")
        sys.stdout.flush()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings


def set_cursor_position(row, col):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save terminal settings
    try:
        sys.stdout.write(f"\033[{row};{col}H")
        sys.stdout.flush()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings
