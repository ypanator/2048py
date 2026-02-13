from constants import *
import curses

def drawBoard(scr, board):
    # grid is 9x9
    # curses cords are (y, x)
    # window top left is (0, 0)

    width = 6
    y, x = 2, curses.COLS // 2 - 4
    scr.addstr(y, x, f"+{"-"*width}+{"-"*width}+{"-"*width}+{"-"*width}+")
    y += 1
    for row in board:
        num1 = row[0] if row[0] is not None else " "
        num2 = row[1] if row[1] is not None else " "
        num3 = row[2] if row[2] is not None else " "
        num4 = row[3] if row[3] is not None else " "
        scr.addstr(y, x, 
            f"|{num1: ^{width}}|{num2: ^{width}}|{num3: ^{width}}|{num4: ^{width}}|")
        scr.addstr(y+1, x, f"+{"-"*width}+{"-"*width}+{"-"*width}+{"-"*width}+")
        y += 2

    scr.addstr(y+1, x+12, "W: up")
    scr.addstr(y+2, x,    "A: left")
    scr.addstr(y+2, x+21, "D: right")
    scr.addstr(y+3, x+11, "S: down")
    scr.addstr(y+5, x+5,  "Q: quit; E: restart")

    scr.refresh()