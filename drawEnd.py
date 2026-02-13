import curses

def drawEnd(scr, maxNum):
    scr.addstr(curses.LINES // 2, curses.COLS // 2, f"Game Over! Max number: {maxNum}")
    scr.refresh()