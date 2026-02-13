from constants import *
import curses

def drawBoard(scr, board):
    # grid is 9x9
    # curses cords are (y, x)
    # window top left is (0, 0)

    width = 6
    y, x = 4, curses.COLS // 2 - 4
    scr.addstr(y, x, f"+{"-"*width}+{"-"*width}+{"-"*width}+{"-"*width}+")
    y += 1
    for row in board:
        num1 = row[0] if row[0] is not None else " "
        num2 = row[1] if row[1] is not None else " "
        num3 = row[2] if row[2] is not None else " "
        num4 = row[3] if row[3] is not None else " "
        scr.addstr(y, x, 
            f"|{num1: ^{width}}|{num2: ^{width}}|{num3: ^{width}}|{num4: ^{width}}|")
        y += 1
        scr.addstr(y, x, f"+{"-"*width}+{"-"*width}+{"-"*width}+{"-"*width}+")
        y += 1
    scr.refresh()