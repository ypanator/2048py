from curses import wrapper
from drawBoard import drawBoard
from handleInput import handleInput
from calcBoard import calcBoard, placeNewNum
from constants import *
from scanBoard import scanBoard
from drawEnd import drawEnd
import time

# TODO: fix input handling
# TODO: add keybinds on board draw
# TODO: clean draw end

def main(stdscr):
    state = play
    curChar = None
    board = [[None] * 4 for _ in range(4)]
    maxNum = placeNewNum(board, [(0, 0)])

    drawBoard(stdscr, board)
    while curChar != q:
        data = scanBoard(board)
        if data.emptySpots == []:
            state = end
        action = handleInput(curChar)

        while action == error:
            curChar = stdscr.getch()
            action = handleInput(curChar)

        if state == end:
            drawEnd(stdscr, maxNum)
            while curChar != q or curChar != e:
                curChar = stdscr.getch()
                time.sleep(0.1)
            state = play
            board = [[None] * 4 for _ in range(4)]
            maxNum = placeNewNum(board, [(0, 0)])
            continue
        elif state == play:
            calcBoard(board, action)
            placeNewNum(board, data.emptySpots)
            drawBoard(stdscr, board)
        else:
            raise ValueError("Invalid state")

        curChar = stdscr.getch()

wrapper(main)
# https://docs.python.org/3/howto/curses.html``