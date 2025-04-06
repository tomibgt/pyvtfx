# conftest.py

import os
import pytest

def pytest_terminal_summary(terminalreporter):
    # Clear the screen before printing the summary
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

    terminalreporter.write_sep("=", "Test Summary")
    # Print the final test summary after all tests
    terminalreporter.write(f"Passed: {len(terminalreporter.stats.get('passed', []))}\n")
    terminalreporter.write(f"Failed: {len(terminalreporter.stats.get('failed', []))}\n")
    terminalreporter.write(f"Skipped: {len(terminalreporter.stats.get('skipped', []))}\n")
