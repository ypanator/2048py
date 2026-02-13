import curses

def drawEnd(scr, maxNum):
    scr.addstr(curses.LINES // 2, curses.COLS // 2 - 8, f"Game Over! Max number: {maxNum}")
    scr.addstr(curses.LINES // 2 + 1, curses.COLS // 2 - 10, "Press E to restart, Q to quit.")
    scr.refresh()